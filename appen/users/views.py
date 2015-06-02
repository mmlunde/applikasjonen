from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

def user_login(request):
    context = {}
    if request.method == 'POST':
    	username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
    		login(request, user)
    		return redirect('frontpage')
    	else:
    		context['login_failed'] = True

    return render(request, 'users/login.html', context)

def user_logout(request):
	logout(request)
	return redirect('frontpage')

def change_user_info(request):
	context = {}
	if request.method == "POST":
		user = request.user
		first_name = request.POST.get('firstname_change')
		user.first_name = first_name
		last_name = request.POST.get('lastname_change')
		user.last_name = last_name 
		email = request.POST.get('email_change')
		user.email = email
		user.save()
		context['user_saved'] = True
	return render(request, 'users/account_settings.html', context)

def user_register(request):
	context = {}
	if request.method == "POST":
		user = User()
		user.first_name = request.POST.get('firstname')
		user.last_name = request.POST.get('lastname')
		user.email = request.POST.get('email')
		user.username = request.POST.get('username')	
		user.set_password(request.POST.get('password'))
		if User.objects.filter(username=user.username).exists():
			context['username_taken'] = True
		elif User.objects.filter(email=user.email).exists():
			context['email_taken'] = True	
		else:	
			user.save()
			context['user_saved'] = True
	return render(request, 'users/register.html', context)

