from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import checkinform, checkoutform
from .models import Passenger, State, Destination
from .serializers import stateSerializer, destinationSerializer, passengerSerializer, paymentSerializer

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

class PassengerView(APIView):
    def post(self, request):
        data = request.data

        serializer = passengerSerializer(data = data)

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
            if (passenger.amt_paid-passenger.fare)>=0:
                passenger.paid = True
                passenger.save()
            if serializer.is_valid():
                serializer.save()
                return Response({
                'data':serializer.data,
                'status':status.HTTP_202_ACCEPTED
                })

class CheckoutView(APIView):
    def put(self, request):

        data = request.data
        fingerprint = request.data.get('fingerprint')

        passenger = Passenger.objects.get(fingerprint = fingerprint)
        if passenger is None:
            return Response({
                'message':'passenger doesn\'t exist',
                'status':status.HTTP_400_BAD_REQUEST
            })
        
        else:
            if passenger.paid == True:
                return Response({
                'message':"Thank You for riding in this bus",
                'status':status.HTTP_202_ACCEPTED
                })
            else:
                return Response({
                'message':"Please pay the fare",
                'status':status.HTTP_402_PAYMENT_REQUIRED
                })


# def Checkin(request):
#     form = checkinform()
#     if request.method=='POST':
        
#         # context = {'form':form}
#         form = checkinform(request.POST)
#         if form.is_valid():
#             passenger = form.save(commit=True)
#             passenger.save()
#             return redirect('checkin')

        
        # passenger = Passenger.objects.create(
        #     destination = destination,
        #     fare = fare
        # )
        # passenger.save()
    
        
    # return render(request, 'ticketing/checkin.html', {'form':form})

# def Checkout(request):
#     form = checkoutform()
    
#     if request.method=='POST':
#         fingerprint = request.POST.get('fingerprint')

#         passenger = Passenger.objects.get(fingerprint = fingerprint)
    
#         if passenger.paid and (int(passenger.fare-passenger.amt_paid)==0):
#             return redirect('checkout-success')
#         else:
#             return redirect('checkout-fail')
    
#     return render(request, 'ticketing/checkout.html', {'form':form})

# def CheckoutSuccess(request):
#     return render(request, 'ticketing/checkoutSuccess.html')


# def CheckoutFail(request):
#     return render(request, 'ticketing/checkoutfail.html')