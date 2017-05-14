from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from website.views import *
from tiendita.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name = "index"),
    url(r'^index_menu$', index_menu, name = "index_menu"),
    url(r'^products/', include('website.productUrls', namespace = 'products')),
    url(r'^menu/', include('website.menuUrls', namespace = 'menu')),
    url(r'^contacto/$', contacto, name = "contacto"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
