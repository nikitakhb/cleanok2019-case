"""Benefits application models."""

from django.db import models


class Benefit(models.Model):
    title = models.CharField('Заголовок', max_length=40)
    content = models.CharField('Описание', max_length=140)
    img = models.ImageField(
        'Фотография', upload_to='images/', blank=True)

    class Meta:
        """Benefit model metadata."""

        ordering = ['id']
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title
