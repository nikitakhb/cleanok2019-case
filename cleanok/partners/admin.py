from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.encoding import force_text
from .models import PartnerCategory, Partner


def get_picture_preview(obj):
    if obj.pk:
        src = obj.img.url
        title = obj.name
        return mark_safe(f'<a href="{src}" target="_blank"><img src="{src}"\
             alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>')

    return "(выберите картинку и сохраните для предпросмотра)"


get_picture_preview.short_description = "Предпросмотр"


class PartnerInline(admin.StackedInline):
    model = Partner
    extra = 0
    fields = ['get_edit_link', 'name', 'img', get_picture_preview]
    readonly_fields = ["get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if obj.pk:
            url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[
                          force_text(obj.pk)])
            text = f'Редактировать в отдельном окне'
            return mark_safe(f'<a href="{url}">{text}</a>')
        return "сохраните и продолжите редактирование для создания ссылки"
    get_edit_link.short_description = "Изменить ссылку"


@admin.register(PartnerCategory)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    fields = ['name', ]
    inlines = [PartnerInline]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ['category', 'name', get_picture_preview]
    readonly_fields = [get_picture_preview]
