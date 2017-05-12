from django.conf.urls import url
from website.views import *

urlpatterns = [
	#url(r'^(?P<tipo>[A-Z][a-z]+)/$',  menu, name='menu'),
	url(r'^$', index, name='index'),
]
