# Generated by Django 3.1.6 on 2021-02-07 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО инструктора')),
                ('about', models.TextField(blank=True, verbose_name='О себе')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название маршрута')),
                ('type', models.CharField(choices=[('Пеший', 'On Foot'), ('Велосипедный', 'On Bike'), ('Водный', 'On Boat')], db_index=True, default='Пеший', max_length=12, verbose_name='Тип маршрута')),
                ('short_desc', models.TextField(verbose_name='Краткое описание')),
                ('long_desc', models.TextField(verbose_name='Полное описание')),
                ('location', models.CharField(db_index=True, max_length=200, verbose_name='Местоположение')),
                ('duration', models.IntegerField(db_index=True, verbose_name='Продолжительность')),
                ('length', models.FloatField(db_index=True, verbose_name='Длина')),
                ('complexity', models.IntegerField(choices=[(1, 'Easy'), (2, 'Advanced'), (3, 'Hard')], db_index=True, default=1, verbose_name='Сложность')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания маршрута')),
                ('featured_photo', models.URLField(verbose_name='Фото для оформления маршрута')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Маршрут доступен для проведения')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='routes', to='travelapp.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='RoutePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='travelapp.route')),
            ],
        ),
    ]
