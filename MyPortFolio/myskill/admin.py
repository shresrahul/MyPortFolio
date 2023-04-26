from django.contrib import admin
from .models import Myskill

class MyskillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_level')

# Register your models here.
admin.site.register(Myskill, MyskillAdmin)
