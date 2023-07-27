from django.shortcuts import render

from django.http import HttpResponse

from .models import Flight,Airport
# Create your views here.

def index(request):
    # return HttpResponse("Praise the Lord")
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })