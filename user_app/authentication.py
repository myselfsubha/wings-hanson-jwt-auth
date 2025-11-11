# app/authentication.py
import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User
from datetime import datetime

class JWTAuthentication(authentication.BaseAuthentication):
    """
    Simple stateless JWT auth.
    Expects Authorization: Bearer <token>
    """

    keyword = "Bearer"

    def authenticate(self, request):
        header = authentication.get_authorization_header(request).split()
        if not header:
            return None  # no auth header -> let other authenticators or permission_classes handle

        if len(header) != 2:
            raise exceptions.AuthenticationFailed("Invalid Authorization header.")

        prefix = header[0].decode()
        token = header[1].decode()

        if prefix != self.keyword:
            return None

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token has expired.")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed("Invalid token.")

        user_id = payload.get("user_id")
        if user_id is None:
            raise exceptions.AuthenticationFailed("Invalid payload.")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found.")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is inactive.")

        # Optionally attach payload to user (or return token)
        return (user, token)
