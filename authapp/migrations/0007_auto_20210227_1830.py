# Generated by Django 3.1.6 on 2021-02-27 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210227_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Женский'), (2, 'Мужской')], db_index=True, default=2, verbose_name='Пол'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 15, 30, 29, 626139, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
    ]