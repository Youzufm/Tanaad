# Generated by Django 4.2.7 on 2023-12-08 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_teachers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teachers',
            new_name='Teacher',
        ),
    ]