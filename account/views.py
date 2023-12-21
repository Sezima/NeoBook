# views.py
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from social_django.utils import load_strategy, load_backend
from social_core.exceptions import AuthForbidden
from .serializers import GoogleAuthSerializer
from django.shortcuts import redirect
from django.contrib.auth import login
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from .models import MyUser

class GoogleAuthAPIView(APIView):
    serializer_class = GoogleAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                user = self.authenticate_user(serializer.validated_data['access_token'])
                login(request, user)
                return Response({'message': 'Аутентификация прошла успешно'}, status=status.HTTP_200_OK)
            except AuthForbidden as e:
                return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def authenticate_user(self, request, access_token):
    strategy = load_strategy(request)
    backend = load_backend(strategy=strategy, name='google-oauth2', redirect_uri=None)
    user = backend.do_auth(access_token, response=None)
    if user and user.is_active:
        return user
    else:
        raise AuthForbidden('Аутентификация не удалась')





def google_callback(request):
    # Получаем информацию о пользователе из Google OAuth
    google_user = request.social_auth.get('google-oauth2')

    # Проверяем, существует ли пользователь с таким email
    user_email = google_user.email
    existing_user = MyUser.objects.filter(email=user_email).first()

    if existing_user:
        # Если пользователь уже существует, авторизуем его
        login(request, existing_user)
    else:
        # Если пользователь не существует, создаем нового
        user = MyUser.objects.create_user(username=google_user.uid, email=user_email)
        user.google_uid = google_user.uid
        user.google_email = user_email
        user.save()
        login(request, user)

    return redirect('/')