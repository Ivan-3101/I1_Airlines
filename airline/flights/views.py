from django.shortcuts import render

from django.http import HttpResponse

from .models import Flight,Airport
# Create your views here.

def index(request):
    # return HttpResponse("Praise the Lord")
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })

def flight(request,flight_id):
    # first step is getting the fligh
    # whose id is entered 
    flight = Flight.objects.get(pk=flight_id)
    # pk for primary key, id= flight is also ok

    return render(request,"flights/flight.html",{
        "flight" : flight,
        "passengers" : flight.passengers.all()
    })