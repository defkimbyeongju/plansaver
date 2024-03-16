from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts, NewDeposits, NewSavings

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class DepositProductsSerializer(serializers.ModelSerializer):
    # options = DepositOptionsSerializer(many=True, read_only=True)  # Assuming options is the related name from DepositProducts to DepositOptions

    class Meta:
        model = DepositProducts
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'

class NewDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDeposits
        fields = '__all__'

class NewSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewSavings
        fields = '__all__'

'''
class Test(serializers.Serializer):
    product = DepositProductsSerializer()
    # 하나만 받아오면 
    # options = DepositOptionsSerializer()
    # 여러개 받아오면
    options = DepositOptionsSerializer(many=True)
'''
