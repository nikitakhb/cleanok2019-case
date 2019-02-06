from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Benefit


def get_picture_preview(obj):
    if obj.pk:
        src = obj.img.url
        title = obj.title
        return mark_safe(f'<a href="{src}" target="_blank"><img src="{src}"\
             alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>')

    return '(выберите картинку и сохраните для предпросмотра)'


get_picture_preview.short_description = 'Предпросмотр'


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    """Model admin for benefits."""

    fields = ('title', 'content', 'img', get_picture_preview,)
    readonly_fields = (get_picture_preview,)
