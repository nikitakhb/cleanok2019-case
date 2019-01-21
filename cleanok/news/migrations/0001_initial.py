# Generated by Django 2.1.5 on 2019-01-21 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('preview', models.TextField(verbose_name='Анонс')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['created_date', 'date'],
            },
        ),
        migrations.CreateModel(
            name='NewsRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_news', to='news.News')),
                ('to_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_news', to='news.News')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='related',
            field=models.ManyToManyField(blank=True, through='news.NewsRelationship', to='news.News'),
        ),
        migrations.AlterUniqueTogether(
            name='newsrelationship',
            unique_together={('from_news', 'to_news')},
        ),
    ]
