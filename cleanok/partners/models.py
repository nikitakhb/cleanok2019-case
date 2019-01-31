from django.db import models


class PartnerCategory(models.Model):
    name = models.CharField("Тип партнера", max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип партнера"
        verbose_name_plural = "Типы партнеров"


class Partner(models.Model):
    name = models.CharField("Наименование", max_length=64)
    img = models.ImageField(
        "Фото", upload_to='images/', blank=True)
    category = models.ForeignKey(
        PartnerCategory, verbose_name="Тип", related_name="partners", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
