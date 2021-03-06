from django.db import models


class News(models.Model):
    """News model."""

    title = models.CharField(max_length=64, verbose_name='Заголовок')
    preview = models.TextField(verbose_name='Анонс')
    text = models.TextField(verbose_name='Содержание')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    date = models.DateField(
        blank=True, null=True, verbose_name='Дата публикации')
    related = models.ManyToManyField('self', through='NewsRelationship',
                                     symmetrical=False, blank=True)

    def publish(self):
        self.date = models.DateTimeField(auto_now_add=True, blank=True)
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        """News model metadata."""

        ordering = ['created_date', 'date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewsRelationship(models.Model):
    """News relationship model."""

    from_news = models.ForeignKey('News', related_name='from_news',
                                  on_delete=models.CASCADE)
    to_news = models.ForeignKey('News', related_name='to_news',
                                on_delete=models.CASCADE, verbose_name='Новость')

    def __str__(self):
        return str(self.to_news)

    class Meta:
        """News relationship model metadata."""

        unique_together = ('from_news', 'to_news')
        verbose_name = 'Читайте также'
        verbose_name_plural = 'Читайте также'
