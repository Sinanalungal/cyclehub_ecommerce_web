# Generated by Django 4.2.6 on 2023-11-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0023_remove_coupons_user_coupons_is_listed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='valid_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]