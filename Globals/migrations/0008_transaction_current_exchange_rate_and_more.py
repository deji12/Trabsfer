# Generated by Django 5.0.1 on 2024-01-18 10:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0007_rename_has_recipient_transaction_has_receipient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='current_exchange_rate',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=uuid.UUID('63fd3095-7e74-4cde-8afa-fcc397ce3f58'), max_length=225),
        ),
    ]
