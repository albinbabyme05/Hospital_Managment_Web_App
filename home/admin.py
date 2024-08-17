from django.contrib import admin

# import model
from . models import Departments, Doctors, Booking

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'bookingDate', 'booked_on')
admin.site.register(Booking, BookingAdmin)