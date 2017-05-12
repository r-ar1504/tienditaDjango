from django.conf.urls import url

from views import *

urlpatterns = [
	url(r'^$', product_index,  name = 'products-index'),
]
