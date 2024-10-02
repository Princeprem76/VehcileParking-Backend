from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Payments, notify
from .serializer import PaymentSerializer, notifySerializers


# Create your views here.
class Payment(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        print(data['service'])
        pay = Payments.objects.create(
            price=int(float(data["price"])),
            payment_method=data["payment_method"],
            user=self.request.user,
            service_id=data["service"],
            payment_done=True,
        )
        return Response({"message": "Payment Successful!"}, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        payments = Payments.objects.filter(user=request.user).order_by('-id')
        serializer = PaymentSerializer(payments, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    
class NotificationData(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        notification = notify.objects.filter(user=self.request.user).order_by('-created')
        noti_serialize = notifySerializers(notification, many=True)
        return Response(noti_serialize.data, status=status.HTTP_200_OK)