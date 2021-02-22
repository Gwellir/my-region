# Generated by Django 3.1.6 on 2021-02-22 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210222_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 12, 29, 45, 649291, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
    ]
