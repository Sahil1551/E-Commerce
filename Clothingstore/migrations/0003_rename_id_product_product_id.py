# Generated by Django 4.1.7 on 2023-09-24 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0002_alter_product_id_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='product_id',
        ),
    ]
