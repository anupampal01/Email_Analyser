from django.shortcuts import render
from .utils import get_basic_dns_records

def dns_lookup(request):
    results = {}
    if request.method == "POST":
        domain = request.POST.get("domain")
        results = get_basic_dns_records(domain)
    return render(request, 'dns_check.html', {"results": results})
