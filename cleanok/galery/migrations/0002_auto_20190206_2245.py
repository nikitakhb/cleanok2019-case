# Generated by Django 2.1.5 on 2019-02-06 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='picture',
            new_name='cover',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='picture',
            new_name='img',
        ),
    ]
