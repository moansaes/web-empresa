from django.shortcuts import render
from service.models import Service
# Create your views here.

def home(request):
    return render(request, "home/home.html")

def market(request):
    return render(request, "home/market.html")










