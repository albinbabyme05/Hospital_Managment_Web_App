from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.hello),
    path('about/', views.about),
    path('booking/', views.booking),
    path('doctor', views.doctors),
    path('contact', views.contact)
]