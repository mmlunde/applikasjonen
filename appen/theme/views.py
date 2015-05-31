from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from theme import models
from theme.models import Comment

# Create your views here.
def frontpage(request):
	if request.method == "POST":
		new_comment_text = request.POST.get('new_comment')
		new_comment = Comment()
		new_comment.comment = new_comment_text
		new_comment.comment_by = request.user
		new_comment.comment_datetime = timezone.now()
		new_comment.save()

	comments = Comment.objects.all()
	page_number = request.GET.get('page', 1)
	paginator = Paginator(comments, 5)
	try: 
		comments = paginator.page(page_number)
	except PageNotAnInteger:
		comments = paginator.page(1)
	except EmptyPage:
		comments = paginator.page(paginator.num_pages)

	context = {
		#'user': user, 
		'comments': comments,
	}
				
	return render(request, 'theme/frontpage.html', context)
