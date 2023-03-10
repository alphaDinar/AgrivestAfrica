# Generated by Django 4.1.7 on 2023-03-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0011_rename_country_profile_cor_profile_id_pic_back_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='other_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
