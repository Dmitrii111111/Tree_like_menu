"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from importlib.util import find_spec

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from project import settings
from menu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('home'))),
    # path('', include('menu.urls'))
]

# URL-шаблоны для каждого приложения будут доступны по URL-адресам, начинающимся с имени приложения.
for app in settings.MENUEXAMPLE_APPS:
    mod = app + '.urls'
    if find_spec(mod):
        urlpatterns.append(path(app + '/', include(mod)))


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound