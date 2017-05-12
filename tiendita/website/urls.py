from django.conf.urls import url, include

from website.views import *

urlpatterns = [
	url(r'^products/', include('website.productUrls', namespace = 'products')),
	url(r'^clients/', include('website.menuUrls', namespace = 'menu')),

]
