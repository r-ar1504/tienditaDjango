from django.shortcuts import render
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
	print 'This is : %s' % (tipo)
	for product in products:
		print product.nombre
	return render(request, 'listBodyTemplate.html', context)

#---------------------------------------------------------Tiendita homepage.
def index(request):
	context = {}
	return render(request, 'index.html', context)

#---------------------------------------------------------Tiendita shopping cart.
def shopping_cart(request):
	context = {}
	return render(request, 'shoppingCart.html', context)
