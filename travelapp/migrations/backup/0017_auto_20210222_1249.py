# Generated by Django 3.1.6 on 2021-02-22 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0016_auto_20210221_1616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TripOption',
            new_name='TripOptionAvailable',
        ),
    ]
