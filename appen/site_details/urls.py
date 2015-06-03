from django.conf.urls import include, patterns, url
#importing views form other directories
from theme import views as theme_views
from users import views as users_views

urlpatterns = patterns('',
	url(r'^(\d+)/$', theme_views.comment_details, name='comment_details'),
	url(r'^(\d+)/adding_likes/(\d+)$', theme_views.add_likes, name='add_likes'),
	url(r'^$', users_views.change_user_info, name='change_user_info'),
)
