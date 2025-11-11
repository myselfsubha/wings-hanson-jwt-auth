# from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import status
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# from user_app.serializers import UserSerializer

# class LoginApiView(APIView):
#     def post(self, request):
#         # Get the username and password from the request
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # If the user is authenticated, return a success response
#             refresh = RefreshToken.for_user(user)
#             return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
#         return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

# class RegistrationView(APIView):
#     def post(self, request):
#         # Get the username and password from the request
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             # if User.objects.filter(email=serializer.validated_data['email']).exists():
#             #     return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#             # if serializer.validated_data['password']!=request.data['password2']:
#             #     return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Logout(APIView):
        def post(self, request):
            try:
                refresh_token = request.data.get('refresh')  # Get refresh token from request
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist the token
                return Response({"detail": "Refresh token blacklisted."}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)  
# 
# 


# Custom Authentication using the Jwtstateless

# app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.conf import settings
from datetime import datetime, timedelta
import jwt

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User

# Helper to create token
def create_jwt_for_user(user):
    """
    payload contains minimal claims. Add more as needed.
    """
    exp_seconds = getattr(settings, "JWT_EXP_DELTA_SECONDS", 3600)
    now = datetime.utcnow()
    payload = {
        "user_id": user.id,
        "email": user.email,
        "role": user.role,
        "iat": now,
        "exp": now + timedelta(seconds=exp_seconds)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    # In PyJWT >= 2.0 encode returns a str; if bytes decode to str
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = UserSerializer(user).data
            return Response({"message": "User created", "user": data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({"detail": "User disabled."}, status=status.HTTP_403_FORBIDDEN)

        token = create_jwt_for_user(user)
        return Response({"token": token, "user": UserSerializer(user).data}, status=status.HTTP_200_OK)
