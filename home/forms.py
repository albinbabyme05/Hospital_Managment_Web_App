from django import forms

#import model name
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
            'bookingDate' : DateInput()
        }
        
        labels = {
            'p_name' : "Patient Name:",
            'p_email' : "Patient Email:",
            'p_phone': "Patient Phone:" ,
            'doc_name': "Doctor Name:",
            'bookingDate': "Booking Date:", 
        }