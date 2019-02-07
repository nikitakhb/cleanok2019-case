"""Certificates application models."""

from django.db import models


class Certificate(models.Model):
    """Ceritificate model."""

    name = models.CharField('Наименование сертификата', max_length=64)
    company = models.CharField('Наименование компании', max_length=64)
    image = models.ImageField('Изображение',
                              upload_to='images/', blank=True)

    class Meta:
        """Certificate model metadata."""
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
