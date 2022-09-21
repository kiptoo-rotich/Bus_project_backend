from django.db import models
from django.db.models.fields import CharField, EmailField


class Bus(models.Model):
    bus_company = models.CharField(max_length=30)
    source= models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    plate_number=models.CharField(max_length=9)
    seats = models.IntegerField(default=62)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField((u"Date"), blank=False)
    time = models.TimeField((u"Departure Time"), blank=False)
    contact = models.IntegerField(null=False,default=+254)

    @classmethod
    def search_buses(cls, source, destination, bus_company):
        return cls.objects.filter(source__icontains=source , destination__icontains=destination,bus_company__icontains=bus_company).all()
        
    def bus_details(cls):
        bus_details_list=cls.objects.all()
        return bus_details_list 

    def save_bus(self):
        self.save()

    def delete_bus(self):
        self.delete()
    
    @classmethod
    def update_bus(self):
        bus=Bus.objects.get_or_create()
        return bus

    def __str__(self):
        return self.bus_company

class Driver(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    id_number=models.IntegerField(unique=True)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.first_name
