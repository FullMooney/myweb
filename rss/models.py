# -*- coding: utf-8 -*-
from __future__ import unicode_literals #python 2.x support

from django.db import models
# from django.utils.encoding import python_2_unicode_compatible #outdated
from six import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Rss(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField('url', unique=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Categories(models.Model):
	Title = models.CharField(max_length=40, null=False)

	class Admin:
		pass

@python_2_unicode_compatible
class TagModel(models.Model):
	Title = models.CharField(max_length=20, null=False)

	class Admin:
		pass

@python_2_unicode_compatible
class Entries(models.Model):
	Title = models.CharField(max_length=80, null=False)
	Content = models.TextField(null=False)
	#created = models.DateTimeField(auto_now_add=True)
	#created = models.DateTimeField(null=True)
	created = models.DateTimeField(auto_now=True)
	Category = models.ForeignKey(Categories)
	Tags = models.ManyToManyField(TagModel)
	Comments = models.PositiveSmallIntegerField(default=0, null=True)

	class Admin:
		pass

	def get_absolute_url(self):
		return '/entry/%d/222' % self.id

@python_2_unicode_compatible
class Comments(models.Model):
	Name = models.CharField(max_length=20, null=False)
	Password = models.CharField(max_length=32, null=False)
	Content = models.TextField(max_length=2000, null=False)
	created = models.DateTimeField(auto_now=True)
	#created = models.DateTimeField(auto_now_add=True)
	#created = models.DateTimeField(null=True)
	Entry = models.ForeignKey(Entries)
