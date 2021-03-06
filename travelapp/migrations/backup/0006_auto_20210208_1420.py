# Generated by Django 3.1.6 on 2021-02-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_auto_20210208_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveler',
            name='subscribed_to',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribed_to', to='travelapp.Traveler', verbose_name='Подписчики'),
        ),
    ]
