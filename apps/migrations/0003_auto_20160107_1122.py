# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_picture_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=70, null=True, verbose_name=b'Main Heading', blank=True)),
                ('content', models.CharField(max_length=70, null=True, verbose_name=b'Content', blank=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'images/slider', verbose_name=b'Slider Image')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(default=b'', max_length=250, verbose_name=b'Email')),
                ('message', models.TextField(verbose_name=b'Message')),
                ('name', models.CharField(max_length=250, verbose_name=b'Name')),
                ('is_approved', models.BooleanField(default=False, verbose_name=b'Testimonial approved or Not')),
                ('phone', models.CharField(max_length=500, null=True, verbose_name=b'Number', blank=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'images/picture', verbose_name=b'Product Image'),
        ),
    ]
