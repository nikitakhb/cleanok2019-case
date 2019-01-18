from django.db import models


class Album(models.Model):
    title = models.CharField("Название", max_length=20)
    picture = models.ImageField(
        "Обложка", upload_to='images/', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.title


class Picture(models.Model):
    album = models.ForeignKey(
        Album, verbose_name="Альбом", related_name="albums", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=20)
    picture = models.ImageField(
        "Фотография", upload_to='images/', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.title
