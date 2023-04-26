from django.db import models

# Create your models here.

class PortFolio(models.Model):
    CATEGORY = (
        ('web','Web'),
        ('app','App'),
        ('logo','Logo'),
        ('social','Social Media'),
    )
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100, choices= CATEGORY)
    client_name = models.CharField(max_length=250)
    project_date = models.DateField()
    project_url = models.URLField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.project_name

