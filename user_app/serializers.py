# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     password2= serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields=['username', 'email', 'password', 'password2']
#         extra_kwargs={
#             'password':{'write_only':True},
#         }

#     def save(self):
#         if self.validated_data['password'] != self.validated_data['password2']:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
        
#         if User.objects.filter(email=self.validated_data['email']).exists():
#             raise serializers.ValidationError({'error':'Email already exists.'})
        
#         user = User(username=self.validated_data['username'], email=self.validated_data['email'])
#         user.set_password(self.validated_data['password'])
#         user.save()
#         return user


# Second Way using Custom User Model

from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("id", "email", "password", "role")
        read_only_fields = ("id",)

    def create(self, validated_data):
        raw_password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(raw_password)
        user.save()
        return user

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "role", "is_active", "created_at")
