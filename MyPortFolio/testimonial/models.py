from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonial/images/')