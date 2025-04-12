from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def email_upload_view(request):
    return render(request, 'upload.html')  # Make sure 'upload.html' exists

def contact_view(request):
    return render(request, 'contact.html')
