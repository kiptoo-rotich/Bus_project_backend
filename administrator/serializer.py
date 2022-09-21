from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Bus
from user.models import Book, Ticket

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bus
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields='__all__'

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','title', 'ticket_id','user', 'content', 'category','created', 'modified')
