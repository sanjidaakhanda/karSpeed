# Generated by Django 4.2.7 on 2023-12-17 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karDetail', '0004_alter_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]