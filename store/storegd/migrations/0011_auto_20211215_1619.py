# Generated by Django 3.1.4 on 2021-12-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storegd', '0010_auto_20211215_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=False),
        ),
    ]
