# Generated by Django 4.2.6 on 2023-11-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0036_remove_contactform_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='remainingbalance',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
    ]
