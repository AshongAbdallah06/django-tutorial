from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Flight, Passenger


# Create your views here.
def index(request):
    all_flights = Flight.objects.all()
    return render(request, "flights/index.html", {"flights": all_flights})


def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(
        request,
        "flights/flight.html",
        {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "non_passengers": Passenger.objects.exclude(flights=flight).all(),
        },
    )


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)

    return HttpResponseRedirect(reverse("flight", args=[flight_id]))
