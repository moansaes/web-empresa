

# Create your views here.
from market.models import Market
from django.shortcuts import render

def market(request):
    market=Market.objects.all()
    return render(request, "market/market.html", {'market': market})