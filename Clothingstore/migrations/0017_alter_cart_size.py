# Generated by Django 4.1.7 on 2023-09-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0016_alter_cart_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
