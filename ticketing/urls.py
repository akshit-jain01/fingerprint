from django.contrib import admin
from django.urls import path

from .views import stateView, destinationView, PassengerView, CheckoutView

urlpatterns = [
    path('states/',stateView.as_view(), name='states'),
    path('destinations/',destinationView.as_view(), name='destinations'),
    path('passengerreg/',PassengerView.as_view(), name='passenger'),
    path('checkout/',CheckoutView.as_view(), name='checkout'),
]