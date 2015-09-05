from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'corplaw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^forum/logo.jpg', '../corplaw.templates.forum.logo.jpg', name='logo.jpg'), 
    url(r'^forum/AshwaniBraj.jpg', '../corplaw.templates.forum.AshwaniBraj.jpg', name='AshwaniBraj.jpg'),
    url(r'^forum/Shantanu.jpg', '../corplaw.templates.forum.Shantanu.jpg', name='Shantanu.jpg'),
    url(r'^admin/', include(admin.site.urls)),
)
