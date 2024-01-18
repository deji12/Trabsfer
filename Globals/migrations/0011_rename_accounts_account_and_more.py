# Generated by Django 5.0.1 on 2024-01-18 12:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0010_accounts_alter_transaction_transaction_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=uuid.UUID('2f8ca70e-9a99-4667-a51e-7ced5cbbedca'), max_length=225),
        ),
    ]
