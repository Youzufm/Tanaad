# Generated by Django 4.2.7 on 2023-12-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_exams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=35)),
                ('Phone', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
                ('Shift', models.CharField(max_length=10)),
            ],
        ),
    ]
