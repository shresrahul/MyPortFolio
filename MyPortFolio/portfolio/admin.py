from django.contrib import admin
from .models import PortFolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type', 'title')
    search_fields = ('title', 'project_type',)
    list_filter = ('title', 'project_type',)

# Register your models here.

admin.site.register(PortFolio, PortfolioAdmin)

admin.site.site_title = 'Portfolio'
admin.site.site_header = 'My Portfolio'
admin.site.index_title = 'Admin Panel'