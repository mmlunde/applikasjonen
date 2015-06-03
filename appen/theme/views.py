from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from theme import models
from theme.models import Comment

# Create your views here.

def frontpage(request):
	#retreaving the text typed into the input fields in frontpage.html
	#and saving the text in as a comment.
	if request.method == "POST":
		new_comment_text = request.POST.get('new_comment')
		new_comment = Comment()
		new_comment.comment = new_comment_text
		new_comment.comment_by = request.user
		new_comment.comment_datetime = timezone.now()
		new_comment.save()

	#getting all the comments form class Comment
	comments = Comment.objects.all()
	page_number = request.GET.get('page', 1)
	#Limits to 5 comments per page
	paginator = Paginator(comments, 5)
	try: 
		comments = paginator.page(page_number)
	except PageNotAnInteger:
		comments = paginator.page(1)
	except EmptyPage:
		comments = paginator.page(paginator.num_pages)
	#making a dictonary 	
	context = { 
		'comments': comments,
	}
				
	return render(request, 'theme/frontpage.html', context)
	

def add_likes (request, user_id, comment_id): 
	comment = Comment.objects.get(pk=comment_id)
	comment.likes = comment.likes + 1
	comment.save()
	data = {'comment_updated': comment.likes}
	#Refering to the appen.js file
	return JsonResponse(data)


def comment_details(request, comment_id):
	comments = Comment.objects.all().filter(id=comment_id)
	context = { 
		'comments': comments,
	}
	return render(request, 'theme/comment_detail.html', context)
