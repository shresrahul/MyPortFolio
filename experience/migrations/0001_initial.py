# Generated by Django 4.1.7 on 2023-03-09 03:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=150)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(default='Present')),
                ('company', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('duties', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]