from django.urls import path
from . import views

urlpatterns = [
    path('', views.spoof_detection, name='spoof_detection'),
]
