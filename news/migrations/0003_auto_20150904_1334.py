# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150903_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyphoto',
            name='photo',
            field=models.ImageField(upload_to='history_photos'),
        ),
    ]
