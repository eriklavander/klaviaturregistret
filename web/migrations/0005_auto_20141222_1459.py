# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20141220_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='text',
            field=models.TextField(max_length=8192, verbose_name=b'Beskrivning'),
            preserve_default=True,
        ),
    ]
