# Generated by Django 4.1.4 on 2022-12-19 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('crop', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='farmCrop_pics')),
                ('price', models.FloatField()),
                ('service_charge', models.FloatField()),
                ('ros_min', models.FloatField()),
                ('ros_max', models.FloatField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=800)),
                ('location', models.CharField(max_length=200)),
                ('units_total', models.PositiveIntegerField()),
                ('units_left', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField(default=1)),
                ('service_charge', models.FloatField()),
                ('image', models.ImageField(default='default.jpg', upload_to='trade_pics')),
                ('description', models.TextField(max_length=800)),
                ('ros_min', models.FloatField()),
                ('ros_max', models.FloatField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available', max_length=40)),
                ('Farm', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
