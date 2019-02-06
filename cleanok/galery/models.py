"""Galery application models."""

from django.db import models


class Album(models.Model):
    """Album model."""

    title = models.CharField('Название', max_length=20)
    cover = models.ImageField(
        'Обложка', upload_to='images/', blank=True)

    class Meta:
        """Album model metadata."""

        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        """Represent album as a string."""

        return self.title


class Picture(models.Model):
    """Picture model."""

    album = models.ForeignKey(
        Album, verbose_name='Альбом', related_name='pictures', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=20)
    img = models.ImageField(
        'Фотография', upload_to='images/', blank=True)

    class Meta:
        """Picture model metadata."""

        ordering = ['title']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        """Represent picture as a string."""

        return self.title
