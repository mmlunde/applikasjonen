from django.conf.urls import include, patterns, url
from site_details import views

urlpatterns = patterns('',
	url(r'^$', views.account_settings, name='account_settings'),
	url(r'^$', views.comment_rows, name='comment_rows'),
)
