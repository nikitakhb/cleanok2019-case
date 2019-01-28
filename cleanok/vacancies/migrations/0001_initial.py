# Generated by Django 2.1.5 on 2019-01-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название города')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименованеи вакансии')),
                ('requirements', models.TextField(max_length=1024, verbose_name='Требования')),
                ('main_responsibilities', models.TextField(max_length=2048, verbose_name='Основные обязанности')),
                ('cities', models.ManyToManyField(related_name='vacancies', to='vacancies.City', verbose_name='Города')),
            ],
        ),
    ]