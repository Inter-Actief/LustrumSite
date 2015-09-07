# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPhoto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsBase',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryEntry',
            fields=[
                ('newsbase_ptr', models.OneToOneField(primary_key=True, to='news.NewsBase', serialize=False, auto_created=True, parent_link=True)),
            ],
            bases=('news.newsbase',),
        ),
        migrations.CreateModel(
            name='NewsEntry',
            fields=[
                ('newsbase_ptr', models.OneToOneField(primary_key=True, to='news.NewsBase', serialize=False, auto_created=True, parent_link=True)),
            ],
            bases=('news.newsbase',),
        ),
        migrations.AddField(
            model_name='newsbase',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historyphoto',
            name='history_entry',
            field=models.ForeignKey(to='news.HistoryEntry'),
        ),
    ]
