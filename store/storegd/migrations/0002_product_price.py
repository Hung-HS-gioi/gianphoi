# Generated by Django 3.1.4 on 2021-12-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storegd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=False),
        ),
    ]