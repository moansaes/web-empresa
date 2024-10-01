from service.models import Service
from django.shortcuts import render

def service(request):
    service=Service.objects.all()
    return render(request, "service/service.html", {'service': service})
