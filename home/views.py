from django.shortcuts import render
from django.http import HttpResponse


# import models
from .models import Departments
from .models import Doctors

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    return render(request, 'booking.html')


def doctors(request):
    dict_doc = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_doc)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    dict_department = {
        'dept' : Departments.objects.all()
    }
    return render(request, 'department.html', dict_department)