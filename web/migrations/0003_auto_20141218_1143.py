# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20141216_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='venue',
            field=models.OneToOneField(related_name='address', blank=True, to='web.Venue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='venue',
            field=models.ForeignKey(related_name='contacts', to='web.Venue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='description',
            name='venue',
            field=models.ForeignKey(related_name='descriptions', to='web.Venue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='venue',
            field=models.ForeignKey(related_name='images', to='web.Venue'),
            preserve_default=True,
        ),
    ]
