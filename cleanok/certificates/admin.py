from django.contrib import admin
from django.utils.html import mark_safe

from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Model admin for certificates."""

    list_display = ('name', 'company')
    ordering = ('company', 'name')
    fields = ('name', 'company', 'image', 'view_image')
    readonly_fields = ('view_image',)

    def view_image(self, obj):
        return mark_safe(f'<a href="{obj.image.url}"><div style="background-image:url({obj.image.url});'
                         f'max-height:300px;'
                         f'max-width:300px;'
                         f'height:{obj.image.height}px;'
                         f'width:{obj.image.width}px;'
                         f'background-repeat: no-repeat;'
                         f'background-size: cover;'
                         f'background-position: center;"></div>'
                         f'</a>')

    view_image.short_description = "Предпросмотр изображения"
