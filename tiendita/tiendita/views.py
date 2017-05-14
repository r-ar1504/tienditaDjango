from django.shortcuts import render

def index_menu(request):
	context = {}
	return render(request, 'index.html', context)


def login(request):
	context = {}
	return render(request, 'registration/login.html', context)

def logout(request):
	context = {}
	return render(request, 'registration/logged_out.html', context)
