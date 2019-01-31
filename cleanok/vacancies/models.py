from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField('Название города', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Vacancy(models.Model):
    name = models.CharField('Наименованеи вакансии', max_length=64)
    cities = models.ManyToManyField(City, related_name='vacancies', verbose_name='Города')
    requirements = models.TextField('Требования', max_length=1024)
    main_responsibilities = models.TextField('Основные обязанности', max_length=2048)
    condition = models.TextField('Условия', max_length=1024)
    contact = models.CharField('Контактные данные', max_length=32)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
