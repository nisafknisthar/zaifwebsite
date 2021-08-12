# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20160107_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='single',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to=b'images/single pic', verbose_name=b'Single Tile Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='featured',
            field=models.BooleanField(default=False, verbose_name=b'Featured Product or Not'),
        ),
    ]
