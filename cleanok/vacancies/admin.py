"""Vacancies application models."""

from django.contrib import admin

from .models import City, Vacancy


class CityInline(admin.TabularInline):
    """City inline admin model."""

    model = City


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Vacancies model admin."""

    list_display = ('name',)
    filter_horizontal = ('cities',)


admin.site.register(City)
