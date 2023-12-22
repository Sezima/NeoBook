from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .utils import send_welcome_mail
from rest_framework.authtoken.views import ObtainAuthToken


from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
                'password_confirm': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
            },
            required=['username', 'email', 'password', 'password_confirm'],
        ),
        responses={
            201: "Successfully signed up!",
            400: "Bad Request",
        },
        manual_parameters=[
            openapi.Parameter(
                'activation_code',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Activation code for the user's account.",
            ),
        ],
    )
    def post(self, request):
        """
        Register a new user.
        """
        data = request.data
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()

            # Your activation logic here
            activation_code = user.activation_code
            activation_url = f"http://localhost:8000/api/v1/account/activate/{activation_code}"

            # You may want to send this URL as part of your response
            response_data = {
                "message": "Successfully signed up! Check your email for activation instructions.",
                "activation_url": activation_url,
                "activation_code": {activation_code},
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class ActivationView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response("Your successfully activated!", status=status.HTTP_200_OK)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)  # Используйте метод get_or_create
        return Response({'token': token.key, 'user_id': user.pk})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logout', status=status.HTTP_200_OK)


