from django.shortcuts import render
import os
from .parser import parse_email
from django.conf import settings

def email_upload_view(request):
    data = None
    if request.method == "POST":
        email_file = request.FILES['email_file']
        file_path = os.path.join(settings.BASE_DIR, "uploads", email_file.name)

        with open(file_path, 'wb+') as f:
            for chunk in email_file.chunks():
                f.write(chunk)

        data = parse_email(file_path)  # Assuming parse_email returns parsed data to be displayed

    return render(request, 'email_parser.html', {"data": data})
