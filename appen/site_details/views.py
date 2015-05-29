from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
		
	comments = user.comments.all()
	page_number = request.GET.get('page')
	paginator = Paginator(notes, 5)
	try: 
		comment = paginator.page(page_number)
	except PageNotAnInteger:
		comment = paginator.page(1)
	except EmptyPage:
		comment = paginator.page(paginator.num_pages)

	context = {
		'user': user, 
		'comments': comments,
	}
	return render(request, 'theme/frontpage.html')

