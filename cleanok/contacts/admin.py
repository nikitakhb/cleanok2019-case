from django.contrib import admin
from .models import Contact, TypeContact


@admin.register(TypeContact)
class TypeContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['type', 'text']
    pass
