# Generated by Django 3.1.4 on 2021-12-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storegd', '0002_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
