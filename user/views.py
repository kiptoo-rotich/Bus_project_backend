import json
from difflib import SequenceMatcher

import requests
from administrator.models import Bus
from administrator.serializer import BusSerializer,BookingSerializer, TicketSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from requests.auth import HTTPBasicAuth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from user.forms import BusForm, UserRegistrationForm
from user.models import Book, Ticket

from .permissions import IsAdminOrReadOnly

# from .mpesa_credentials import LipanaMpesaPpassword, MpesaAccessToken


def index_user(request):
    if request.method == 'POST':
        form=BusForm(request.POST,request.FILES)
        if form.is_valid():
            source=form.cleaned_data['source']
            destination=form.cleaned_data['destination']
            bus_company=form.cleaned_data['bus_company']
            search_bus=Bus.search_buses(source,destination,bus_company)
            if search_bus:
                messages.success(request, 'Found some buses for you')
            else:
                messages.error(request, 'Oops! No buses found from your search.')
            return render(request, 'main/home.html',{'form':form,"buses":search_bus}) 
        else:
            messages.warning(request,"No available buses.")
    else:
        form = BusForm()
    return render(request,'main/home.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('django_registration_complete')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


class BusList(APIView):
    def get(self,request,format=None):
        all_buses=Bus.objects.all()
        serializers=BusSerializer(all_buses,many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = BusSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BusDetails(APIView):
    def get(self,request, id):
        try:
            bus= Bus.objects.get(id=id)
            serializers = BusSerializer(bus)
            return Response(serializers.data)
        except Bus.DoesNotExist:
            return Http404

class Booking(APIView):
    def get(self,request):
        all_seats=Book.objects.all()
        serializers=BookingSerializer(all_seats,many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = BookingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)