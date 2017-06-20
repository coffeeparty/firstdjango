# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.urls import reverse

class Record(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, unique=True)
	image = models.ImageField(upload_to='records')
	content = models.TextField()
	draft = models.BooleanField(default=False)
	updated= models.DateField(auto_now=True, auto_now_add=False)
	published = models.DateField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['-published'] # Like in coding, when you do -1, you start from the latest. So this 
		## means that when you view you are seeing starting from the last
	def __unicode__(self):  
		return str(self.title)

	def get_absolute_url(self):
		return reverse('records_detail', kwargs={'pk' :self.pk}) ##call the url you created /// kwargs is key dictionary argument
# if you use python 3 it is def__str__(self):
		##													return self.title