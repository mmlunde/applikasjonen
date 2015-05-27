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

def user_register(request):
	context = {}
	if request.method == "POST":
		user = User()
		user.fName = request.POST.get('firstname')
		user.lName = request.POST.get('lastname')
		user.email = request.POST.get('email')
		user.username = request.POST.get('username')	
		user.set_password(request.POST.get('password'))
		user.save()
		context['user_saved'] = True
	return render(request, 'users/register.html', context)

