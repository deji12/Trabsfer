# Generated by Django 5.0.1 on 2024-01-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='has_recipient',
            field=models.BooleanField(default=False),
        ),
    ]