from django.db import models

# Create your models here.

class Slinks(models.Model):
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
