# Generated by Django 2.1.5 on 2019-01-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'Сертификат', 'verbose_name_plural': 'Сертификаты'},
        ),
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, upload_to='certificates/', verbose_name='Изображение'),
        ),
    ]
