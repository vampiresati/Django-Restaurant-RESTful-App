# Generated by Django 2.2.7 on 2019-11-29 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchenapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KitchenUser',
            new_name='User',
        ),
    ]
