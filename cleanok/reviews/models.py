from django.db import models
from datetime import datetime

YEAR_CHOICES = []
for r in range(2000, (datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class Review(models.Model):
    company = models.CharField("Компания", max_length=120)
    year = models.IntegerField(
        "Год написания", default=datetime.now().year, choices=YEAR_CHOICES)
    picture = models.ImageField(
        "Фотография", upload_to='images/', blank=True)

    class Meta:
        ordering = ['year', 'company']
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекоментации"

    def __str__(self):
        return f'{self.company}, {self.year} год'
