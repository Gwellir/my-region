# Generated by Django 3.1.7 on 2021-04-21 11:59

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0013_auto_20210419_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routephoto',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='route_photos', verbose_name='Фото для оформления маршрута'),
        ),
    ]
