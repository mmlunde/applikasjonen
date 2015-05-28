from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', include('theme.urls')),
	url(r'^users/', include('users.urls')),
	url(r'^site_details/', include('site_details.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
