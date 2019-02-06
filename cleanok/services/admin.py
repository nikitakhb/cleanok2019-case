"""Services application models."""

from django.contrib import admin

from .models import Service, ServiceCategory, WorkItem


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """Model admin for service categories."""

    list_display = ('name',)
    search_fields = ('name', 'url_link',)
    ordering = ('name',)


class WorkItemInline(admin.TabularInline):
    """Model admin for work items."""

    model = WorkItem
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Model admin for services."""

    list_display = ('category', 'name',)
    ordering = ('category', 'name',)
    autocomplete_fields = ('category',)
    inlines = (WorkItemInline, )
