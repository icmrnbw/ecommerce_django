# Generated by Django 4.1 on 2022-10-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_shippingdetails_delete_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingdetails',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='payment_click',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='payment_payme',
            field=models.BooleanField(default=False),
        ),
    ]
