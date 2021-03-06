# Generated by Django 3.1.6 on 2021-02-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='group_size',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='adults_amount',
            field=models.IntegerField(default=1, verbose_name='Взрослых в вашей группе'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Контактный E-mail'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='contact_phone',
            field=models.CharField(default='+7-999-99-99', max_length=15, verbose_name='Контактный телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='kids_amount',
            field=models.IntegerField(default=0, verbose_name='Детей в вашей группе'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Пожелания'),
        ),
    ]
