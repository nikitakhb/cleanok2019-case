# Generated by Django 2.1.5 on 2019-01-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='vacancy',
            name='condition',
            field=models.TextField(default='', max_length=1024, verbose_name='Условия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='contact',
            field=models.CharField(default='', max_length=32, verbose_name='Контактные данные'),
            preserve_default=False,
        ),
    ]