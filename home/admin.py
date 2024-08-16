from django.contrib import admin

# import model
from . models import Departments, Doctors
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)