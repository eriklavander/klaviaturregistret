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
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=512, verbose_name=b'Adress')),
                ('author', models.ForeignKey(verbose_name=b'Anv\xc3\xa4ndare', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(max_length=128, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=512, verbose_name=b'Beskrivning')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(verbose_name=b'Anv\xc3\xa4ndare', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=128, blank=True)),
                ('image', models.ImageField(upload_to=b'images')),
                ('thumbnail', models.ImageField(upload_to=b'thumbnails', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'Namn')),
                ('audience_min', models.IntegerField(blank=True)),
                ('audience_max', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='venue',
            field=models.ForeignKey(to='web.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='venue',
            field=models.ForeignKey(to='web.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='venue',
            field=models.ForeignKey(to='web.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='venue',
            field=models.OneToOneField(to='web.Venue'),
            preserve_default=True,
        ),
    ]
