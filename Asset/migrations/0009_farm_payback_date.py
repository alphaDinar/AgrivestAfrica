# Generated by Django 4.1.4 on 2022-12-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset', '0008_trade_payback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='payback_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
