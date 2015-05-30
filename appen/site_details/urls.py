from django.conf.urls import include, patterns, url
from site_details import views

urlpatterns = patterns('',
	url(r'^$', views.account_settings, name='account_settings'),
	#url(r'^$', views.change_firstname, name='change_firstname'),
	#url(r'^$', views.change_lastname, name='change_lastname'),
	#url(r'^$', views.change_email, name='change_email'),
)
