from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
	comment = models.TextField()
	comment_by = models.ForeignKey(User, related_name="written_comments")
	comment_datetime = models.DateTimeField()

	def __unicode__(self):
		return u'%s' % self.comment

	#class Meta: 
		#ordering = ['-pub_date']
		