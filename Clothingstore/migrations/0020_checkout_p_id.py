# Generated by Django 4.1.7 on 2023-10-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothingstore', '0019_checkout_p_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='p_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
