#-*- coding: utf-8-*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import *
from website.forms import ContactoForm
import smtplib
from django.shortcuts import redirect

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
	print products
	return render(request, 'listBodyTemplate.html', context)

		#List items by type
def listSearchItems(request, tipo):
	products = Producto.objects.all().filter(tipo = tipo)
	print products
	search_query = request.GET.get("q")
	filtered_products = products.filter (Q(nombre__contains=search_query))
	print filtered_products
	context = {'products': filtered_products, 'tipo': tipo}
	return render(request, 'listBodyTemplate.html', context)

	#Add item generic view
class NewItem(CreateView):
	model = Producto
	fields = ['id', 'nombre', 'tipo', 'descripcion', 'precio', 'foto']

	#Edit item generic view
class EditItem(UpdateView):
	model = Producto
	fields = ['id', 'nombre', 'tipo', 'descripcion', 'precio', 'foto']

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

#---------------------------------------------------------Tiendita contacto.
def contacto(request):
	form_class = ContactoForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get('nombre', '')
			contact_email = request.POST.get('email', '')
			form_content = request.POST.get('mensaje', '')
			sender = 'scripts@itesm.edu'
			receivers = ['scripts@itesm.edu']
			message = """From: La Tiendita <scripts@itesm.edu>
To: <scripts@itesm.edu>
Subject: Points contact message

Contact name: """ + contact_name + "\n" + "Contact email: " + contact_email + \
                         "\nMessage contents: \n" + form_content
			smtpObj = smtplib.SMTP('localhost')
			smtpObj.sendmail(sender, receivers, message.encode("utf-8"))
			return redirect('index')
	context = {'form':form_class}
	return render(request,'contacto.html',context)
