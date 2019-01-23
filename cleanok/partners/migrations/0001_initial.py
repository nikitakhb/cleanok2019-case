# Generated by Django 2.1.5 on 2019-01-22 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
                ('img', models.ImageField(blank=True, upload_to='images/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='PartnerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Тип партнера')),
            ],
            options={
                'verbose_name': 'Тип партнера',
                'verbose_name_plural': 'Типы партнеров',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='partners.PartnerCategory', verbose_name='Тип'),
        ),
    ]
