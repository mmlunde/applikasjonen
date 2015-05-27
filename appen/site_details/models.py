from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s (%s)' % (self.firstname, self.lastname)