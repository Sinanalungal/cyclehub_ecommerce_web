# Generated by Django 4.2.6 on 2023-11-24 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0032_contactform_time_alter_product_product_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
