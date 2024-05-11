from django.forms import ModelForm

from .models import Passenger

class checkinform(ModelForm):
    
    class Meta:
        model = Passenger
        fields = '__all__'
        # exclude = ['fingerprint']

class checkoutform(ModelForm):
    
    class Meta:
        model = Passenger
        fields = ['fingerprint']