# Generated by Django 5.1.1 on 2024-09-15 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_tag_alter_collection_options_collection_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
