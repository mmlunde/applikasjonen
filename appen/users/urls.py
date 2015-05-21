from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^login$', views.user_login, name='user_login'),
)