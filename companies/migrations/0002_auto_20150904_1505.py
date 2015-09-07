# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='banner',
            name='start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
