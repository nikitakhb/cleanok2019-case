from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.encoding import force_text

from .models import Album, Picture


def get_picture_preview(obj):
    if obj.pk:
        src = obj.picture.url
        title = obj.title
        return mark_safe(f'<a href="{src}" target="_blank"><img src="{src}"\
             alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>')

    return '(выберите картинку и сохраните для предпросмотра)'


get_picture_preview.short_description = 'Предпросмотр'


class PictureInline(admin.StackedInline):
    model = Picture
    extra = 0
    fields = ['get_edit_link', 'title', 'picture', get_picture_preview]
    readonly_fields = ['get_edit_link', get_picture_preview]

    def get_edit_link(self, obj=None):
        if obj.pk:
            url = reverse(
                f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change',
                args=[force_text(obj.pk)])
            text = f'Изменить {obj._meta.verbose_name} в новом окне'
            return mark_safe(f'<a href="{url}">{text}</a>')
        return 'ссылка появится после сохранения записи'
    get_edit_link.short_description = 'Ссылка'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Model admin for albums."""

    list_display = ['title', ]
    fields = ['title', 'picture', get_picture_preview]
    readonly_fields = [get_picture_preview]
    inlines = [PictureInline]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    """Model admin for pictures."""

    fields = ['album', 'title', 'picture', get_picture_preview]
    readonly_fields = [get_picture_preview]
