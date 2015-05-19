# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_tc_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativenote',
            name='note_type',
            field=models.IntegerField(blank=True, null=True, db_index=True, choices=[(1, b'Gri'), (1, b'Kara')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tc_identifier',
            field=models.IntegerField(null=True, verbose_name=b'Tc kimlik numaras\xc4\xb1', blank=True),
        ),
    ]
