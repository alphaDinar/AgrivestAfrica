# Generated by Django 4.1.4 on 2022-12-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset', '0007_alter_farm_name_alter_farm_slug_alter_market_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='payback_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
