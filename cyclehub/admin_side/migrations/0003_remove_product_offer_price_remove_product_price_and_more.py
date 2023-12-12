# Generated by Django 4.2.6 on 2023-10-30 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0002_remove_product_quantity_remove_product_tyre_size_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offer_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='tyresize',
            name='offer_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tyresize',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='tyresize',
            name='product_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='admin_side.product'),
            preserve_default=False,
        ),
    ]