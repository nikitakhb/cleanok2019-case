from django.db import models

# Create your models here.


class Promotion(models.Model):
    name = models.CharField('Название акции', max_length=64)
    description = models.TextField('Описание акции', max_length=1024)
    date_publication = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

