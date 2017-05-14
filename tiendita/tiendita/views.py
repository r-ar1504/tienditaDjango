from django.shortcuts import render

def index_menu(request):
	context = {}
	return render(request, 'index.html', context)
