from django.shortcuts import render
from django.utils import timezone

from site_details.models import User 
from site_details.models import CommentField

# Create your views here.
def account_settings(request):
	return render(request, 'site_details/account_settings.html')

def comment_rows(request):
	if request.method == "POST":
		new_comment_text = request.POST.get('new_comment')
		new_comment = CommentField()
		new_comment.comments = new_comment_text
		new_comment.user = user
		new_comment.comment_by = request.user
		new_comment.comment_datetime = timezone.now()
		new_comment.save()

