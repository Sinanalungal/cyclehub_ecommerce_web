# Generated by Django 4.2.6 on 2023-12-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0039_banners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners',
            name='header',
            field=models.CharField(max_length=100),
        ),
    ]