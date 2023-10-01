# Generated by Django 4.1.7 on 2023-09-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0008_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='prize',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]