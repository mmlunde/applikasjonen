from django.conf.urls import include, patterns, url
from site_details import views as site_details_views
from theme import views as theme_views
from users import views as users_views

urlpatterns = patterns('',
	#url(r'^$', views.account_settings, name='account_settings'),
	#url(r'^$', site_details_views.account_settings, name='account_settings'),
	url(r'^(\d+)/$', theme_views.comment_details, name='comment_details'),
	url(r'^(\d+)/adding_likes/(\d+)$', theme_views.add_likes, name='add_likes'),
	#url(r'^(?P<comment_by>.*)$', theme_views.comment_details, name='comment_details'),
	url(r'^$', users_views.change_user_info, name='change_user_info'),
	#url(r'^$', users_views.change_lastname, name='change_lastname'),
	#url(r'^$', users_views.change_email, name='change_email'),
)
