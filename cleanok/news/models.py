from django.db import models
from django.utils import timezone


class News(models.Model):
    """Новости"""
    author = models.ForeignKey(
        'auth.User', on_delete=models.PROTECT, verbose_name="Автор")
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Содержание")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    published_date = models.DateField(
        blank=True, null=True, verbose_name="Дата публикации")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_date', 'published_date', 'author']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
