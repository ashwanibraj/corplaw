from django.conf.urls import patterns, url
from forum import views

urlpatterns= patterns('',
	url(r'^$', views.homepg, name = 'homepg'),
	url(r'^aboutCLF/$', views.aboutCLF, name = 'aboutCLF'),
	url(r'^keynote/$', views.keynote, name = 'keynote'),
	url(r'^subtheme/$', views.subtheme, name = 'subtheme'),
	url(r'^callforpaper/$', views.callforpaper, name = 'callforpaper'),
	url(r'^advisoryboard/$', views.advisoryboard, name = 'advisoryboard'),
	url(r'^participants/$', views.participants, name = 'participants'),
	url(r'^authors/$', views.authors, name = 'authors'),
	url(r'^sponsers/$', views.sponsers, name = 'sponsers'),
	url(r'^contactus/$', views.contactus, name = 'contactus'),
	url(r'^developerinfo/$', views.developerinfo, name = 'developerinfo'),
)
