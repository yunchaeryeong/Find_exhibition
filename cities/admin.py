# cities/admin.py

from django.contrib import admin
from .models import City

# Register your models here.
admin.site.register(City)

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "place")