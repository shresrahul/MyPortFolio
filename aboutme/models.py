from django.db import models

# Create your models here.

class AboutMe(models.Model):
    intro = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    birthday = models.DateField()
    age = models.IntegerField()
    website = models.CharField(max_length=50)
    degree = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    freelance = models.BooleanField()
    short_desc = models.TextField()
    long_desc = models.TextField()
    photo = models.ImageField(upload_to='about/images/')

