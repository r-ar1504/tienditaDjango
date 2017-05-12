from django.shortcuts import render


def menu_index(request):
	context = {}
	return render(request, 'menu-index.html', context)

def product_index(request):
	context = {}
	return render(request, 'product-index.html', context)

def index(request):
	context = {}
	return render(request, 'index.html', context)
