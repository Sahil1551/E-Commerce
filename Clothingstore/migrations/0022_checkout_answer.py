# Generated by Django 4.1.7 on 2023-10-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0021_remove_checkout_p_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='answer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
