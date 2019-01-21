from django.db import models

# Create your models here.


class Certificate(models.Model):
    """
        Модель "Сертификат", будет отображением имеющихся сертификатов и грамот
    """
    name = models.CharField('Наименование сертификата', max_length=64)
    company = models.CharField('Наименование компании', max_length=64)
    image = models.ImageField('Изображение', upload_to='certificates/', blank=True)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
