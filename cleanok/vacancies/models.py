"""Vacancies models."""
from django.db import models


class City(models.Model):
    """Model admin for vacancy cities."""

    name = models.CharField('Название города', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        """City metadata."""

        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Vacancy(models.Model):
    """Model admin for vacancies."""

    name = models.CharField('Наименованеи вакансии', max_length=64)
    cities = models.ManyToManyField(City, related_name='vacancies', verbose_name='Города')
    requirements = models.TextField('Требования', max_length=1024)
    main_responsibilities = models.TextField('Основные обязанности', max_length=2048)
    condition = models.TextField('Условия', max_length=1024)
    contact = models.CharField('Контактные данные', max_length=32)

    class Meta:
        """Vacancy metadata."""

        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
