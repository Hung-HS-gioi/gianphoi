# Generated by Django 3.1.4 on 2021-12-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storegd', '0004_auto_20211209_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
