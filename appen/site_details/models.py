from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s (%s)' % (self.firstname, self.lastname)


class CommentField(models.Model):
	user = models.ForeignKey(User, related_name='comments')
	comment = models.TextField()
	comment_by = models.ForeignKey(User, related_name="written_comments")
	comment_datetime = models.DateTimeField()

	def __unicode__(self):
		return u'%s' % self.comment

	#class Meta: 
		#ordering = ['-pub_date']