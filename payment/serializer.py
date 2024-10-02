from rest_framework import serializers
from .models import Payments, notify

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class notifySerializers(serializers.ModelSerializer):
    class Meta:
        model = notify
        fields = '__all__'