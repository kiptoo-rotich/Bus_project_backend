# Generated by Django 3.2 on 2022-09-05 13:09

import datetime
from django.db import migrations, models
import jsonfield.fields
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_book_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seat',
            field=jsonfield.fields.JSONField(default=user.models.generate_ticket_id),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 16, 9, 31, 524537)),
        ),
    ]
