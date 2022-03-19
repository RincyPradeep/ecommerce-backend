# Generated by Django 4.0.3 on 2022-03-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name=range(1, 5)),
            preserve_default=False,
        ),
    ]
