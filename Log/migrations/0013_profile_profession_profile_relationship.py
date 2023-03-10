# Generated by Django 4.1.7 on 2023-03-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0012_profile_gender_profile_other_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='relationship',
            field=models.CharField(choices=[('single', 'single'), ('married', 'married')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
