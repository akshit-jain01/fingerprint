from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import checkinform, checkoutform
from .models import Passenger, State, Destination
from .serializers import stateSerializer, destinationSerializer, passengerSerializer, paymentSerializer, FingerprintSerializer, paymentconfirmSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class stateView(APIView):
    def get(self, request):

        data = State.objects.all()
        serializer = stateSerializer(instance = data, many=True)

        return Response({
                'data':serializer.data,
                'status':status.HTTP_200_OK
            })
    
class destinationView(APIView):
    def get(self,request):
        data = Destination.objects.all()
        serializer = destinationSerializer(instance=data, many=True)

        return Response({
            'data':serializer.data,
            'status':status.HTTP_200_OK
        })
    
class FingerprintView(APIView):
    def post(self,request):
        data = request.data

        serializer = FingerprintSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data,
                'status':status.HTTP_201_CREATED
            })
        else:
            return Response({
                'data':serializer.errors,
                'status':status.HTTP_400_BAD_REQUEST
            })

class PassengerView(APIView):
    def put(self, request):

        data = request.data

        passenger = Passenger.objects.last()
        if passenger is None:
            return Response({
                'message':'user doesn\'t exist',
                'status':status.HTTP_400_BAD_REQUEST
            })
        else:
            serializer = passengerSerializer(instance = passenger, data = data)
            # if (passenger.amt_paid-passenger.fare)>=0:
            #     passenger.paid = True
            #     passenger.save()
            if serializer.is_valid():
                serializer.save()
                return Response({
                'data':serializer.data,
                'status':status.HTTP_202_ACCEPTED
                })
class PaymentView(APIView):
    # def post(self, request):
    #     data = request.data

    #     serializer = passengerSerializer(data = data)

    #     passenger = Passenger.objects.last()
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             'data':serializer.data,
    #             'status':status.HTTP_201_CREATED
    #         })
    #     else:
    #         return Response({
    #             'data':serializer.errors,
    #             'status':status.HTTP_400_BAD_REQUEST
    #         })
    
    def put(self, request):

        data = request.data
        fingerprint = request.data.get('fingerprint')

        passenger = Passenger.objects.get(fingerprint = fingerprint)
        if passenger is None:
            return Response({
                'message':'user doesn\'t exist',
                'status':status.HTTP_400_BAD_REQUEST
            })
        
        else:
            serializer = paymentSerializer(instance = passenger, data = data)
            if (passenger.amt_paid-passenger.fare)>0 or (passenger.amt_paid-passenger.fare)==0:
                passenger.paid = True
                passenger.save()
            elif (passenger.amt_paid-passenger.fare)<0:
                passenger.paid=False
                passenger.save()
            if serializer.is_valid():
                serializer.save()
                return Response({
                'data':serializer.data,
                'status':status.HTTP_202_ACCEPTED
                })

class CheckoutView(APIView):
    def get(self, request):

        fingerprint = request.data.get('fingerprint')
        
        passenger = Passenger.objects.get(fingerprint = fingerprint)
        if passenger is None:
            return Response({
                'message':'passenger doesn\'t exist',
                'status':status.HTTP_400_BAD_REQUEST
            })
        
        else:
            if passenger.paid == True:
                passenger.delete()
                return Response({
                'message':"Thank You for riding in this bus",
                'status':status.HTTP_202_ACCEPTED
                })
            else:
                return Response({
                'message':"Please pay the fare",
                'status':status.HTTP_402_PAYMENT_REQUIRED
                })

