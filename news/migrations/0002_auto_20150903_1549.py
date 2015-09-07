# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsbase',
            options={'ordering': ['-publication_date']},
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='publication_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
