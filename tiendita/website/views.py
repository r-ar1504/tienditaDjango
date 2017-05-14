#-*- coding: utf-8-*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

#---------------------------------------------------------Menu & app views.

def menu_index(request):
	context = {}
	return render(request, 'menu-index.html', context)

#---------------------------------------------------------Product's model views.
def product_index(request):
	context = {}
	return render(request, 'product-index.html', context)

	#List items by type
def listItems(request, tipo):
	products = Producto.objects.all().filter(tipo = tipo)
	context = {'products': products, 'tipo': tipo}
	return render(request, 'listBodyTemplate.html', context)

	#Add item generic view
class NewItem(CreateView):
	model = Producto
	fields = ['id', 'nombre', 'tipo', 'descripcion', 'precio']

	#Edit item generic view
class EditItem(UpdateView):
	model = Producto
	fields = ['id', 'nombre', 'tipo', 'descripcion', 'precio']

	#Delete item generic view
class DeleteItem(DeleteView):
	model = Producto
	success_url = reverse_lazy('index')


#---------------------------------------------------------Tiendita homepage.
def index(request):
	context = {}
	return render(request, 'index.html', context)

#---------------------------------------------------------Tiendita shopping cart.
def shopping_cart(request):
	context = {}
	return render(request, 'shoppingCart.html', context)
