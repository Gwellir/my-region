# Generated by Django 3.1.6 on 2021-02-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0011_auto_20210218_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='subbed',
            field=models.IntegerField(default=0, verbose_name='Мест занято'),
        ),
    ]