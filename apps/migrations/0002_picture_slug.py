# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='slug',
            field=models.SlugField(max_length=1000, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
