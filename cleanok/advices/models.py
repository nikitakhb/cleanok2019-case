"""Advices application models."""

from django.db import models
from url_or_relative_url_field.fields import URLOrRelativeURLField


class Advice(models.Model):
    """Advice model."""

    title = models.CharField("Заголовок", max_length=64)
    text = models.TextField("Содержание")
    link = URLOrRelativeURLField("Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        """Recomend model metadata."""

        verbose_name = 'Полезный совет'
        verbose_name_plural = 'Полезные советы'
