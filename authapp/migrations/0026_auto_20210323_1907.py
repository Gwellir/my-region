# Generated by Django 3.1.7 on 2021-03-23 16:07

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0025_auto_20210323_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=authapp.models.get_expiry_datetime, verbose_name='Крайний срок текущей активации'),
        ),
    ]