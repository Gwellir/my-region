# Generated by Django 3.1.6 on 2021-02-22 13:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210222_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 13, 13, 30, 907918, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
    ]
