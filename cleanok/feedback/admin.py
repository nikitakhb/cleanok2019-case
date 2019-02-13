from django.contrib import admin

from .models import FeedBackMessage


@admin.register(FeedBackMessage)
class FeedBackMessageAdmin(admin.ModelAdmin):
    list_display = ('date', '__str__')
