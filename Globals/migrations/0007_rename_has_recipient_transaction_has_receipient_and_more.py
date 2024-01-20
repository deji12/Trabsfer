# Generated by Django 5.0.1 on 2024-01-18 10:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0006_transaction_receipient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='has_recipient',
            new_name='has_receipient',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=uuid.UUID('10ad3d10-1e34-4c43-b3ba-be9b5793a383'), max_length=225),
        ),
    ]