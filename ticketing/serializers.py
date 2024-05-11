from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField

from .models import *

class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class destinationSerializer(serializers.ModelSerializer):
    state = SlugRelatedField(slug_field='name', queryset=State.objects.all())
    class Meta:
        model = Destination
        fields = ['id','name','state']


class passengerSerializer(serializers.ModelSerializer):
    destination = SlugRelatedField(slug_field='name', queryset=Destination.objects.all())
    class Meta:
        model = Passenger
        fields = ['fingerprint', 'destination','fare']


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['fingerprint','amt_paid']


# class paymentconfirmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Passenger
#         fields = ['fingerprint','paid']