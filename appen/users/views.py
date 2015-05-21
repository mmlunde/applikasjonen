from django.contrib.auth import authenticate, login 
from django.shortcuts import render


def user_login(request):
    return render(request, 'users/user_login')