# Generated by Django 4.1.7 on 2023-03-14 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0002_delete_bag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(default='default.jpg', upload_to='message_tags')),
                ('content', models.CharField(max_length=3000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(default='AgrivestAfrica', max_length=300)),
            ],
        ),
    ]
