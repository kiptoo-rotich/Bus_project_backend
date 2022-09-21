from django import forms
from django.db.models.fields import TimeField

from user.forms import DateInput
from administrator.models import Bus,Driver
from django.contrib.auth.models import User

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'
        widgets={
            'date':DateInput(),
        }

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')