# Generated by Django 2.2.7 on 2019-12-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchenapp', '0005_auto_20191201_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
