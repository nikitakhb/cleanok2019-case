from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'url_link']
    ordering = ('name',)


class WorkItemInline(admin.TabularInline):
    model = WorkItem
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')
    ordering = ['category', 'name']
    autocomplete_fields = ['category']
    inlines = (WorkItemInline, )

