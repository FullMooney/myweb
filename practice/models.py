from __future__ import unicode_literals #python 2.x support

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Practice(models.Model):
	filename = models.CharField(max_length=100, blank=False, null=False)
	rangef = models.PositiveIntegerField(blank=False, null=False)
	ranget = models.PositiveIntegerField(blank=False, null=False)
	

	def __str__(self):
		return self.filename
