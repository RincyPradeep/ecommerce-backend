# Generated by Django 4.0.3 on 2022-03-31 05:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='order_amount',
            field=models.FloatField(default=122, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.IntegerField(),
        ),
    ]