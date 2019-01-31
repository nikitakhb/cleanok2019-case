from django.contrib import admin
from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_publication')
    ordering = ['date_publication', 'name']
    readonly_fields = ('date_publication',)
    fields = ('name', 'description', 'date_publication')
