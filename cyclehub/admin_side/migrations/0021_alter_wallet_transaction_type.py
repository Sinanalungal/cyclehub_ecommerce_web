# Generated by Django 4.2.6 on 2023-11-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0020_remove_wallet_coupon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transaction_type',
            field=models.CharField(max_length=50),
        ),
    ]
