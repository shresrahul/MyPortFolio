# Generated by Django 4.1.7 on 2023-03-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0003_aboutme_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
