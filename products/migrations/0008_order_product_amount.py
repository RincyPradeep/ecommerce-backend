# Generated by Django 4.0.3 on 2022-04-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_amount',
            field=models.FloatField(default=1000, max_length=25),
            preserve_default=False,
        ),
    ]
