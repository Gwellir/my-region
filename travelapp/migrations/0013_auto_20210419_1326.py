# Generated by Django 3.1.7 on 2021-04-19 10:26

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0012_auto_20210418_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='featured_photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='img', verbose_name='Фото для оформления маршрута'),
        ),
        migrations.AlterField(
            model_name='route',
            name='gpx_track',
            field=models.FileField(blank=True, upload_to='tracks', verbose_name='Трек маршрута в формате GPX'),
        ),
        migrations.AlterField(
            model_name='routephoto',
            name='image',
            field=models.ImageField(upload_to='route_photos'),
        ),
    ]
