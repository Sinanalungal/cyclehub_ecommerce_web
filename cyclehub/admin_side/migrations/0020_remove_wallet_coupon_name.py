# Generated by Django 4.2.6 on 2023-11-16 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0019_wallet_coupon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='coupon_name',
        ),
    ]
