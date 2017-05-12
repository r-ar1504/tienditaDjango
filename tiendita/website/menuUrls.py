from django.conf.urls import url

from views import *

urlpatterns = [
	url(r'^$', menu_index,  name = 'menu-index'),
]
