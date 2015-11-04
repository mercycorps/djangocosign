# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocosign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='countries',
            field=models.ManyToManyField(related_name='countries', verbose_name=b'Accessible Countires', to='djangocosign.Country', blank=True),
        ),
    ]
