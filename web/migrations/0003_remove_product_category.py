# Generated by Django 4.0.3 on 2022-03-07 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
