from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Review


def get_picture_preview(obj):
    if obj.pk:
        src = obj.picture.url
        title = obj.company
        return mark_safe(f'<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>')

    return "(выберите картинку и сохраните для предпросмотра)"


get_picture_preview.short_description = "Предпросмотр"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = ["company", "year", "picture", get_picture_preview]
    readonly_fields = [get_picture_preview]
