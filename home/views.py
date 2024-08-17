from django.shortcuts import render
from django.http import HttpResponse


# import models
from .models import Departments
from .models import Doctors

#import form
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.POST:
        form = BookingForm(request.POST)
        #Need To validate csrf_token, form, emial_field_other required.
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    else:   
        form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request, 'booking.html', dict_form)


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