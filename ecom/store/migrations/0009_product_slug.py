# Generated by Django 5.1.1 on 2024-09-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_collection_level_collection_lft_collection_rght_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
