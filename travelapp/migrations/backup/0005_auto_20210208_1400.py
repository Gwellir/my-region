# Generated by Django 3.1.6 on 2021-02-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_auto_20210208_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='subscribed_to',
            field=models.ManyToManyField(blank=True, to='travelapp.Instructor', verbose_name='Подписки'),
        ),
    ]
