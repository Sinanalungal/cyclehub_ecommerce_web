# Generated by Django 4.2.6 on 2023-11-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0003_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='kerala', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='full_name',
            field=models.CharField(default='sinan', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(default='9999765483', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='pincode',
            field=models.CharField(default='232323', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='kerala', max_length=100),
            preserve_default=False,
        ),
    ]
