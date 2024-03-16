from rest_framework import serializers
from .models import Exchange_rate

class Exchange_rateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange_rate
        fields = '__all__'
