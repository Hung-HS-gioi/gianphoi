# Generated by Django 3.1.4 on 2021-12-10 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storegd', '0007_product_ditail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
