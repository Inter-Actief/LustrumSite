# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banners')),
                ('link', models.URLField()),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField()),
            ],
            options={
                'ordering': ['?'],
            },
        ),
    ]
