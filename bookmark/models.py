from __future__ import unicode_literals #python 2.x support

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User # for edit

# Create your models here.

@python_2_unicode_compatible
class Bookmark(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField('url', unique=True)
	owner = models.ForeignKey(User, null=True) # for edit
	visiters = models.IntegerField(blank=True, null=True, default=0)

	def __str__(self):
		return self.title
