from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at")
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    ordering = ('created_at',)


admin.site.register(Contact, ContactAdmin)
