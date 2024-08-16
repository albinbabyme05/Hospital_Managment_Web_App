from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello World") 


def about(request):
    return HttpResponse("About Page") 


def booking(request):
    return HttpResponse("Booking Page") 


def doctors(request):
    return HttpResponse("Doctor Page") 


def contact(request):
    return HttpResponse("Contact Page") 