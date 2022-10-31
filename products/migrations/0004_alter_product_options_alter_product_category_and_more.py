# Generated by Django 4.1 on 2022-10-30 14:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_discount_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Created at'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['id', 'name', 'image', 'description'], name='products_ca_id_373932_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'name', 'price', 'category_id', 'image', 'description', 'in_stock', 'created_at', 'discount', 'discount_rate'], name='products_pr_id_4cbdaf_idx'),
        ),
    ]