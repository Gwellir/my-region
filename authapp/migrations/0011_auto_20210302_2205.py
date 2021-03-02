# Generated by Django 3.1.6 on 2021-03-02 19:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210302_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 19, 5, 56, 98937, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
    ]
