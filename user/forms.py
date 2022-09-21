from django.forms import fields, widgets
from administrator.models import Bus
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import Book, SeatNumber


class UserRegistrationForm(UserCreationForm):
    contact=forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'

class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','destination','bus_company', 'date']
        widgets={
            'date':DateInput(),
        }
