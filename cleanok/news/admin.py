"""News application models."""

from django.contrib import admin

from .models import News, NewsRelationship


class RelatedNewsInline(admin.StackedInline):
    model = NewsRelationship
    fk_name = 'from_news'
    extra = 0
    fields = ('to_news',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Model admin for news."""

    list_display = ('title', 'date',)
    list_filter = ('date',)
    inlines = (RelatedNewsInline,)
