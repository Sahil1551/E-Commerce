# Generated by Django 4.1.7 on 2023-09-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0009_remove_cart_image_remove_cart_prize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.IntegerField(max_length=5),
        ),
    ]
