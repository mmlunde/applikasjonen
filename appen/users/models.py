from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	username = models.CharField(max_lenght=50)
	email = models.EmailField()
	firstname = models.CharField(max_lenght=50)
	lastname = models.CharField(max_lenght=100)