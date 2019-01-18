from django.contrib import admin
from .models import *

# Register your models here.


class CityInline(admin.TabularInline):
    model = City


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('cities',)


admin.site.register(City)
