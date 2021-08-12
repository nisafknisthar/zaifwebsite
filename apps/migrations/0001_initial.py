# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, verbose_name=b'Name', blank=True)),
                ('slug', models.SlugField(max_length=1000, unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, verbose_name=b'Name', blank=True)),
                ('email', models.EmailField(max_length=70, null=True, verbose_name=b'Email ID', blank=True)),
                ('message', models.TextField(max_length=70, null=True, verbose_name=b'Message', blank=True)),
                ('phone', models.CharField(max_length=250, null=True, verbose_name=b'Phone_number', blank=True)),
            ],
            options={
                'verbose_name': 'Contactus ',
                'verbose_name_plural': 'Contactus ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=70, null=True, verbose_name=b'Main Heading', blank=True)),
                ('content', models.CharField(max_length=70, null=True, verbose_name=b'Content', blank=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'images/picture', verbose_name=b'Work Image')),
                ('featured', models.BooleanField(default=False, verbose_name=b'Featured Course or Not')),
                ('category', models.ForeignKey(to='apps.Category')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(default=b'Site Name', max_length=255)),
                ('email', models.EmailField(max_length=70, unique=True, null=True, blank=True)),
                ('fb_url', models.URLField(default=b'', verbose_name=b'Facebook', blank=True)),
                ('twitter_url', models.URLField(default=b'', verbose_name=b'Twitter', blank=True)),
                ('linkedin_url', models.URLField(default=b'', verbose_name=b'Linkedin', blank=True)),
                ('logo', models.ImageField(default=b'', upload_to=b'images/logo', verbose_name=b'logo 125*100 px')),
                ('maintenance_mode', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
            bases=(models.Model,),
        ),
    ]
