from django.contrib import admin
from django.urls import path

from .views import stateView, destinationView, PassengerView, CheckoutView, FingerprintView, PaymentView, SecretView

urlpatterns = [
    path('states/',stateView.as_view(), name='states'),
    path('destinations/',destinationView.as_view(), name='destinations'),
    path('fingerprint/',FingerprintView.as_view(), name='fingerprint'),
    path('passengerreg/',PassengerView.as_view(), name='passenger'),
    path('payment/',PaymentView.as_view(), name='payment'),
    path('checkout/',CheckoutView.as_view(), name='checkout'),
    # path('secret/',SecretView.as_view(), name='secret'),
]