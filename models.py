from django.db import models
from django.utils import timezone
from django.utils.timezone import utc
from django.contrib import admin

from django.contrib.auth.models import User, UserManager

import datetime, time, logging


TITLE_CHOICES = (
    ('mr', 'Mr.'),
    ('mrs', 'Mrs.'),
    ('ms', 'Ms.'),
)


class Country(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, blank=True)
    iso_two_letters_code = models.CharField(unique=True, max_length=2, db_index=True)
    created = models.DateTimeField(auto_now=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=False, blank=True, null=True)

    class Meta:
        ordering = ['iso_two_letters_code', 'name',]
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return self.name + " (%s)" % self.iso_two_letters_code

    def save(self, *args, **kwargs):
        ''' On save, update timestamps as appropriate'''
        if kwargs.pop('new_entry', True):
            self.created = datetime.datetime.utcnow().replace(tzinfo=utc)
        else:
            self.updated = datetime.datetime.utcnow().replace(tzinfo=utc)
        return super(Country, self).save(*args, **kwargs)


class Office(models.Model):
    long_name = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    name = models.CharField(max_length=3, db_index=True)
    country = models.ForeignKey(Country, help_text="Select a country")
    created_by = models.ForeignKey(User, related_name='office_created_by')
    created = models.DateTimeField(auto_now=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=False, blank=True, null=True)

    class Meta:
        ordering = ['country', 'name',]
        verbose_name = "Office"
        verbose_name_plural = "Offices"
        unique_together = (("name", "country"),)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps as appropriate'''
        if kwargs.pop('new_entry', True):
            self.created = datetime.datetime.utcnow().replace(tzinfo=utc)
        else:
            self.updated = datetime.datetime.utcnow().replace(tzinfo=utc)
        return super(Office, self).save(*args, **kwargs)


class UserProfile(models.Model):
    title = models.CharField(blank=True, null=True, max_length=3, choices=TITLE_CHOICES)
    name = models.CharField("Given Name", blank=True, null=True, max_length=100)
    employee_number = models.IntegerField("Employee Number", blank=True, null=True)
    user = models.OneToOneField(User, unique=True, related_name='userprofile')
    country = models.ForeignKey(Country, blank=True, null=True)
    countries = models.ManyToManyField(Country, "Accessible Countires", related_name='countries', blank=True)
    modified_by = models.ForeignKey(User, related_name='userprofile_modified_by')
    created = models.DateTimeField(auto_now=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def countries_list(self):
        return ', '.join([x.name for x in self.countries.all()])

    def save(self, *args, **kwargs):
        ''' On save, update timestamps as appropriate'''
        if kwargs.pop('new_entry', True):
            self.created = datetime.datetime.utcnow().replace(tzinfo=utc)
        else:
            self.updated = datetime.datetime.utcnow().replace(tzinfo=utc)
        return super(UserProfile, self).save(*args, **kwargs)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('country','name','title')
    display = 'UserProfile'