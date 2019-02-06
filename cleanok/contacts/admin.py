from django.contrib import admin

from .models import Contact, TypeContact


@admin.register(TypeContact)
class TypeContactAdmin(admin.ModelAdmin):
    """Model admin for contacts types."""
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Model admin for contacts."""

    list_display = ('type', 'text',)
    pass
