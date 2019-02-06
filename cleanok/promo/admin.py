"""Promotion application models."""

from django.contrib import admin

from .models import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    """Model admin for promo."""

    list_display = ('date', 'title',)
    ordering = ('date', 'title',)
    readonly_fields = ('date',)
    fields = ('date', 'title', 'preview', 'text',)
