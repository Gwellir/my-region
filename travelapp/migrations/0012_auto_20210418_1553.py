# Generated by Django 3.1.7 on 2021-04-18 12:53

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0011_route_ya_constructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='featured_photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='static/img', verbose_name='Фото для оформления маршрута'),
        ),
    ]
