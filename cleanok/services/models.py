"""Serivces models."""

from django.db import models


class ServiceCategory(models.Model):
    """Service category model."""

    name = models.CharField('Наименование категории', max_length=32)
    url_link = models.CharField('Ссылка', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        """Service category model metadata."""

        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'


class Service(models.Model):
    """Service model."""

    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE,
                                 verbose_name='Категория услуги',
                                 related_name='services')
    name = models.CharField('Наименование услуги', max_length=32)
    description = models.TextField('Краткое описание', max_length=512)
    min_price = models.FloatField('Минимальная стоимость')

    note = models.TextField('Замечание', max_length=1024)
    warn = models.TextField('Предупреждение', max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        """Service model metadata."""

        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class WorkItem(models.Model):
    """Work item model."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                verbose_name='Услуга', related_name='items')
    name = models.CharField('Наименование пункта', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        """Work item model metadata."""

        verbose_name = 'Пункт работы'
        verbose_name_plural = 'Пункты работ'
