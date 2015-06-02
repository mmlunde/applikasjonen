from django.conf.urls import include, patterns, url

from theme import views

urlpatterns = patterns('',
	url(r'^$', views.frontpage, name='frontpage'),
)