"""Recomend application models."""

from datetime import datetime

from django.db import models

YEAR_CHOICES = []
for r in range(2000, (datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class Recomend(models.Model):
    """Recomend model."""

    title = models.CharField('Компания', max_length=120)
    subt = models.IntegerField(
        'Год написания', default=datetime.now().year, choices=YEAR_CHOICES)
    url = models.ImageField(
        'Фотография', upload_to='images/', blank=True)

    class Meta:
        """Recomend model metadata."""

        ordering = ['subt', 'title']
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекоментации'

    def __str__(self):
        """Return the string representation of the Recomend."""
        return f'{self.title}, {self.subt} год'
