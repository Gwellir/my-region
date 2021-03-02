# Generated by Django 3.1.6 on 2021-03-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_route_is_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='ends_at',
            field=models.DateTimeField(null=True, verbose_name='Время окончания похода'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='starts_at',
            field=models.DateTimeField(db_index=True, verbose_name='Время начала похода'),
        ),
    ]
