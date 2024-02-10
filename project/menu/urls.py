from django.urls import path

from .views import base


urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('company/', base, {'name': 'About'}, name='company'),
    path('prices/', base, {'name': 'Prices'}, name='prices'),
]