from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'email': self.validated_data.get('email', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'age': self.validated_data.get('age', ''),
        'money': self.validated_data.get('money', ''),
        'salary': self.validated_data.get('salary', ''),
        'financial_products': self.validated_data.get('financial_products', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
        # if "password1" in self.cleaned_data:
        #     try:
        #         adapter.clean_password(self.cleaned_data['password1'], user=user)
        #     except DjangoValidationError as exc:
        #         raise serializers.ValidationError(
        #             detail=serializers.as_serializer_error(exc)
        #         )
        # user.save()
        # self.custom_signup(request, user)
        # # setup_user_email(request, user)
        # return user
