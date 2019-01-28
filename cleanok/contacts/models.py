from django.db import models

# Create your models here.


class TypeContact(models.Model):
    """
        Тип контакта. Телефон, Емейл, Адресс,Факс, Сова, Гонец...
    """
    name = models.CharField('Нименование класса', max_length=32)
    eng_name = models.CharField('Псевдоним на английском', max_length=32)

    class Meta:
        verbose_name = 'Тип контакта'
        verbose_name_plural = 'Тип контактов'

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
        Класс контакта. В поле контакт указывается текс, будь то номер телефона или адресс.
        Поле ссылка, не обязательно должна быть указана.
    """
    type = models.ForeignKey(TypeContact, on_delete=models.CASCADE,
                             verbose_name='Тип контакта', related_name='contacts')
    text = models.CharField('Контакт', max_length=128)
    link = models.CharField('Ссылка', max_length=128)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


