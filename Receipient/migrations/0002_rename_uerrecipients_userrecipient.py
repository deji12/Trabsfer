# Generated by Django 5.0.1 on 2024-01-17 20:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receipient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UerRecipients',
            new_name='UserRecipient',
        ),
    ]