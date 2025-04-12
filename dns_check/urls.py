from django.urls import path
from . import views

urlpatterns = [
    path('', views.dns_lookup, name='dns_lookup'),
]
