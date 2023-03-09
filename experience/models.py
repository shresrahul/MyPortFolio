from django.db import models
from ckeditor.fields import RichTextField
from datetime import date, datetime
import datetime

# Create your models here.

class Experience(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    position = models.CharField(max_length=150)
    from_date = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    to_date = models.CharField(max_length=10, default='Present')
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    duties = RichTextField(blank=True, null=True)


