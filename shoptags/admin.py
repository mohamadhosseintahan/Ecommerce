from django.contrib import admin
from shoptags.models import Tag
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        '__str__' , 'active'
    ]
admin.site.register(Tag ,ProductAdmin)