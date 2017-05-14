from django.conf.urls import url
from models import Producto
from views import *

urlpatterns = [
	#url(r'^$', menu_index,  name = 'menu-index'),
	url(r'nuevo/', NewItem.as_view(), name = 'new_item'),
	url(r'editar/(?P<pk>\D+)', EditItem.as_view(), name = 'edit_item'),
	url(r'eliminar/(?P<pk>\D+)', DeleteItem.as_view(), name = 'delete_item'),
	url(r'^(?P<tipo>\D+)/search/$', listSearchItems, name = 'list_search_items'),
	url(r'^(?P<tipo>\D+)/$', listItems, name = 'list_items'),

]
