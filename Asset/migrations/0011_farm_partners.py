# Generated by Django 4.1.4 on 2022-12-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset', '0010_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='partners',
            field=models.ManyToManyField(to='Asset.partner'),
        ),
    ]
