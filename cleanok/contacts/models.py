"""Contacts application models."""

from django.db import models


class TypeContact(models.Model):
    """Contact type model."""

    name = models.CharField('Нименование класса', max_length=32)
    eng_name = models.CharField('Псевдоним на английском', max_length=32)

    class Meta:
        """Contact type model metadata."""

        verbose_name = 'Тип контакта'
        verbose_name_plural = 'Тип контактов'

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Contact model."""

    type = models.ForeignKey(TypeContact, on_delete=models.CASCADE,
                             verbose_name='Тип контакта', related_name='contacts')
    text = models.CharField('Контакт', max_length=128)
    link = models.CharField('Ссылка', max_length=128)

    class Meta:
        """Contact model metadata."""

        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
