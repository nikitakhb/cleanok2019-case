# Generated by Django 2.1.5 on 2019-01-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190117_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Заголовок'),
        ),
    ]