# Generated by Django 4.2.6 on 2023-11-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0004_address_city_address_full_name_address_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_liste',
            field=models.BooleanField(default=True),
        ),
    ]
