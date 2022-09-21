from dataclasses import dataclass
from datetime import datetime
from email.policy import default
from random import random
import uuid
from jsonfield import JSONField
from wsgiref.simple_server import demo_app

from administrator.models import Bus
from django.contrib.auth.models import User
from django.db import models
from django.forms.fields import MultipleChoiceField

def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    ticket_id = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created"]

class Book(models.Model):
    EMPTY = 1
    BOOKED = 2
    CANCELLED = 3
    
    TICKET_STATUSES = (
        (BOOKED, 'Booked'),
        (EMPTY,"Empty"),
        (CANCELLED, 'Cancelled'),
        )

    seat=JSONField(default=2, null=False)
    status = models.IntegerField(choices=TICKET_STATUSES, default=EMPTY)
    created_at = models.DateTimeField(default=datetime.now())

    @classmethod
    def show_bookings(cls,email):
        booking=cls.objects.filter(email=email)
        return booking
        
    def save_booking(self):
        self.save()

    def delete_booking(self):
        self.delete()

    @classmethod
    def update_booking(self):
        book=Book.objects.get_or_create()
        return book

    def __str__(self):
        return self.seat

class SeatNumber(models.Model):
    seat = models.ForeignKey(Book,on_delete=models.CASCADE,)
    amount=models.ForeignKey(Bus,on_delete=models.CASCADE,)
