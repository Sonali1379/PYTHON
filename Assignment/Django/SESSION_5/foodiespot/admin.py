from django.contrib import admin
from foodiespot.models import *
# Register your models here.

class RestaurantDisplay(admin.ModelAdmin):
    list_display = ['name', 'cuisine', 'rating']
    search_fields = ['name', 'cuisine']
    list_filter = ['cuisine']
admin.site.register(Restaurant,RestaurantDisplay)
