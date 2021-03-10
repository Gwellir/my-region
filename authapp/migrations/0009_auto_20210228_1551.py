# Generated by Django 3.1.6 on 2021-02-28 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210227_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='activation_key_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 12, 51, 2, 523869, tzinfo=utc), verbose_name='Крайний срок текущей активации'),
        ),
    ]