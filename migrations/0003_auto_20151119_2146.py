# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangocosign', '0002_auto_20151104_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(related_name='region_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='region_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'Region',
            },
        ),
        migrations.AlterField(
            model_name='office',
            name='name',
            field=models.CharField(max_length=4, db_index=True),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(related_name='countries', on_delete=django.db.models.deletion.DO_NOTHING, blank=True, to='djangocosign.Region', null=True),
        ),
    ]
