from django.db import models

# Create your models here.


class ServiceCategory(models.Model):
    """
        Модель "Категория услуг"
    """
    name = models.CharField('Наименование категории', max_length=32)
    url_link = models.CharField('Ссылка', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'


class Service(models.Model):
    """
        Модель "Услуга"
    """
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Категория услуги',
                                 related_name='services')
    name = models.CharField('Наименование услуги', max_length=32)
    description = models.TextField('Краткое описание', max_length=512)
    min_price = models.FloatField('Минимальная стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class WorkItem(models.Model):
    """
        Модель "Пункт работ"
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', related_name='items')
    name = models.CharField('Наименование пункта', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт работы'
        verbose_name_plural = 'Пункты работ'
