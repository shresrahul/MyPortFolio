# Generated by Django 4.1.7 on 2023-03-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfolio_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_type',
            field=models.CharField(choices=[('web', 'Web'), ('app', 'App'), ('logo', 'Logo'), ('social media', 'Social Media')], max_length=100),
        ),
    ]