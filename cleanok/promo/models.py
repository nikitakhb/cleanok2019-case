from django.db import models


class Promo(models.Model):
    """Promotion model."""

    date = models.DateField('Дата публикации', auto_now_add=True)
    title = models.CharField('Название акции', max_length=64)
    preview = models.TextField('Анонс', max_length=1024)
    text = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        """Promotion model metadata."""

        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
