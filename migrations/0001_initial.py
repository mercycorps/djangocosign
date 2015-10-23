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
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True, null=True, blank=True)),
                ('iso_two_letters_code', models.CharField(unique=True, max_length=2, db_index=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['iso_two_letters_code', 'name'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('long_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('name', models.CharField(max_length=3, db_index=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('country', models.ForeignKey(help_text=b'Select a country', to='djangocosign.Country')),
                ('created_by', models.ForeignKey(related_name='office_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['country', 'name'],
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=3, null=True, choices=[(b'mr', b'Mr.'), (b'mrs', b'Mrs.'), (b'ms', b'Ms.')])),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'Given Name', blank=True)),
                ('employee_number', models.IntegerField(null=True, verbose_name=b'Employee Number', blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('countries', models.ManyToManyField(related_name='countries', db_constraint=b'Accessible Countires', to='djangocosign.Country', blank=True)),
                ('country', models.ForeignKey(blank=True, to='djangocosign.Country', null=True)),
                ('modified_by', models.ForeignKey(related_name='userprofile_modified_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='office',
            unique_together=set([('name', 'country')]),
        ),
    ]
