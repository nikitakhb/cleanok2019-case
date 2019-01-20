# Generated by Django 2.1.5 on 2019-01-19 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190118_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_date', 'published_date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]