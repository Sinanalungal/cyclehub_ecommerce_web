# Generated by Django 4.2.6 on 2023-10-27 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0002_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='additional_images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
    ]