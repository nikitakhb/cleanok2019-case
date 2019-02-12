from django.db import models

from services.models import Service


class Lead(models.Model):
    """Lead model"""

    name = models.CharField('Имя', max_length=32)
    phone = models.CharField('Телефон', max_length=32)
    service = models.ForeignKey(Service, on_delete=models.PROTECT,
                                verbose_name='Услуга', related_name='leads')
    comment = models.TextField('Комментарий', max_length=1024, blank=True)

    def __str__(self):
        return f'{self.name} ({self.phone})'

    class Meta:
        """Lead model metadata."""

        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
