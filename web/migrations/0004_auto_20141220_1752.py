# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20141218_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=128, verbose_name=b'Namn', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=128, null=True, verbose_name=b'Telefon', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
            preserve_default=True,
        ),
    ]
