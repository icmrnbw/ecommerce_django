# Generated by Django 4.1 on 2022-10-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_shippingdetails_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingdetails',
            name='payment_click',
        ),
        migrations.RemoveField(
            model_name='shippingdetails',
            name='payment_payme',
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='payment_type',
            field=models.SmallIntegerField(choices=[(1, 'PayMe'), (2, 'Click')], default=1),
            preserve_default=False,
        ),
    ]
