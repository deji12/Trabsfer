# Generated by Django 5.0.1 on 2024-01-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]