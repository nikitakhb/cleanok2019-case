from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Админка для раздела Новости"""
    list_display = ['title', 'author', 'published_date']
    list_filter = ['author', 'published_date']
