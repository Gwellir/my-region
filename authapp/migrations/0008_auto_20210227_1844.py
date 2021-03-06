# Generated by Django 3.1.6 on 2021-02-27 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210227_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 15, 44, 56, 821576, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Женский'), (2, 'Мужской')], db_index=True, verbose_name='Пол'),
        ),
    ]
