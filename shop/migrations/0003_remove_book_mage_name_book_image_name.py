# Generated by Django 5.1.5 on 2025-01-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_book_mage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='mage_name',
        ),
        migrations.AddField(
            model_name='book',
            name='image_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
