# Generated by Django 3.1.6 on 2021-02-27 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210227_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 15, 24, 1, 936621, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона'),
        ),
    ]
