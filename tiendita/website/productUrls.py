from django.conf.urls import url
from models import Producto
from views import *

urlpatterns = [
	url(r'^$', product_index,  name = 'products-index'),
	url(r'(?P<tipo>\D+)/', listItems, name = 'list_items'),
]
