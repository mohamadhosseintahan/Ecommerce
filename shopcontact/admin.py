from django.contrib import admin

# Register your models here.
from .models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    search_fields = ['text', 'subject']


admin.site.register(ContactUs, ContactAdmin)
