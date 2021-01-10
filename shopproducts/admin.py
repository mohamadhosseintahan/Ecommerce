from django.contrib import admin
from .models import Products, Gallery


# Register your models here.

class ProdustsAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'title', 'price', 'active'
    ]

    class Meta:
        model = Products


admin.site.register(Products, ProdustsAdmin)
admin.site.register(Gallery)
