# Generated by Django 3.2 on 2022-11-03 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220905_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 3, 8, 26, 49, 210905)),
        ),
    ]
