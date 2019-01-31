from django.contrib import admin
from .models import Vacancy, City


class CityInline(admin.TabularInline):
    model = City


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('cities',)


admin.site.register(City)
