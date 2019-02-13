from django.db import models


class FeedBackMessage(models.Model):
    """ FeedBack model """
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    message = models.TextField('Сообщение', max_length=512)
    date = models.DateTimeField('Дата/Время', auto_now=True)

    def __str__(self):
        return self.message[:50]

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
