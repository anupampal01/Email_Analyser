from django.urls import path
from .views import email_upload_view, parse_email
from . import views

urlpatterns = [
    path('', views.email_upload_view, name='email_upload_view'),
    # path('parse/', parse_email, name='parse_email'),
     path('email_parser/', parse_email, name='parse_email'),
]


