# Generated by Django 2.2.7 on 2019-12-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchenapp', '0006_kitchenimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchenimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
