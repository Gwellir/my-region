# Generated by Django 3.1.7 on 2021-04-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0003_auto_20210323_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='contact_phone',
            field=models.CharField(max_length=20, verbose_name='Контактный телефон'),
        ),
    ]
