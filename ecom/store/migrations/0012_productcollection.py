# Generated by Django 5.1.1 on 2024-09-28 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_collection_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_collections', to='store.collection')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_collections', to='store.product')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('collection', 'product')},
            },
        ),
    ]