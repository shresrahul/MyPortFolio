# Generated by Django 4.1.7 on 2023-03-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('photo', models.ImageField(upload_to='testimonial/images/')),
            ],
        ),
    ]
