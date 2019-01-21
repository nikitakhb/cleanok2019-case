from django.db import models
from datetime import datetime

YEAR_CHOICES = []
for r in range(2000, (datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class Recomend(models.Model):
    title = models.CharField("Компания", max_length=120)
    subt = models.IntegerField(
        "Год написания", default=datetime.now().year, choices=YEAR_CHOICES)
    url = models.ImageField(
        "Фотография", upload_to='images/', blank=True)

    class Meta:
        ordering = ['subt', 'title']
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекоментации"

    def __str__(self):
        return f'{self.title}, {self.subt} год'
