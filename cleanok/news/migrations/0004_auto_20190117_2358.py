# Generated by Django 2.1.5 on 2019-01-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190117_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
