# Generated by Django 4.2.6 on 2023-11-12 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0010_ordereditems_orders_delete_order_ordereditems_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='admin_side.orders'),
        ),
    ]
