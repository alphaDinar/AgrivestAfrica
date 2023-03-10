# Generated by Django 4.1.4 on 2022-12-27 12:24

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Asset', '0009_farm_payback_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('location', models.CharField(max_length=300)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
    ]
