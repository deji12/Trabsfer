# Generated by Django 5.0.1 on 2024-01-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0017_alter_transaction_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(max_length=225),
        ),
    ]
