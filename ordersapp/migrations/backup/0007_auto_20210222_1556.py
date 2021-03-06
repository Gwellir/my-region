# Generated by Django 3.1.6 on 2021-02-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210222_1556'),
        ('travelapp', '0017_auto_20210222_1249'),
        ('ordersapp', '0006_auto_20210222_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='options_used',
            field=models.ManyToManyField(to='travelapp.TripOptionAvailable', verbose_name='Дополнительные опции'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('traveler', 'trip')},
        ),
    ]
