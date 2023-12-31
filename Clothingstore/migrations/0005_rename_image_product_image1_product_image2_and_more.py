# Generated by Django 4.1.7 on 2023-09-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0004_alter_product_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=0, upload_to='images/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=0, upload_to='images/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default=0, upload_to='images/products'),
        ),
    ]
