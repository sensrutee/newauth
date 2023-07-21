from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('phonenumber', 'username', 'email', 'password', 'full_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user






# from django.contrib.auth.models import User
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
#
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(min_length=8, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'first_name', 'last_name')
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user