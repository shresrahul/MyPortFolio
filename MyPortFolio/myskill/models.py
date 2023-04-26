from django.db import models


# Create your models here.

class Myskill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_level = models.IntegerField()

    def __str__(self):
        return self.skill_name
