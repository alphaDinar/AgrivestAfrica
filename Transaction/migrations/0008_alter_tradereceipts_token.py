# Generated by Django 4.1.7 on 2023-02-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction', '0007_remove_tradelog_token_tradereceipts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradereceipts',
            name='token',
            field=models.UUIDField(default=1, unique=True),
        ),
    ]
