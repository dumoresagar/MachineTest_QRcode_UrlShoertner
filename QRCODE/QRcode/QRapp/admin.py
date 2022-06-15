from django.contrib import admin
from .models import Url,Website
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ['full_url','short_url']

admin.site.register(Url,UrlAdmin)

admin.site.register(Website)
