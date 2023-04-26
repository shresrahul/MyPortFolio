from django.db import models

# Create your models here.
class Education(models.Model):
    course = models.CharField(max_length=250)
    duration = models.CharField(max_length=50)
    institute = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.course