# Generated by Django 4.0.3 on 2022-04-12 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id']},
        ),
    ]
