from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
	comment = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	comment_by = models.ForeignKey(User, related_name="written_comments")
	comment_datetime = models.DateTimeField()
	

	def __unicode__(self):
		return u'%s' % self.comment
	#making comments appear descending publication date
	class Meta: 
		ordering = ['-comment_datetime']
