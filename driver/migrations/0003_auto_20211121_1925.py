# Generated by Django 3.2.9 on 2021-11-21 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_auto_20211121_0818'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
    ]
