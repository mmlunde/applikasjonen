from django.shortcuts import render


# Create your views here.
def account_settings(request):
	return render(request, 'site_details/account_settings.html')