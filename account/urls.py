from django.urls import path
from .views import GoogleAuthAPIView
from .views import *


urlpatterns = [
    # path('register/', RegisterView.as_view()),
    # path('activate/<str:activation_code>/', ActivationView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),
    # path('reset-password/', ResetPassword.as_view()),
    # path('reset-password-complete/', ResetComplete.as_view()),
    path('google/auth/', GoogleAuthAPIView.as_view(), name='google_auth'),
    path('google/callback/', google_callback, name='google_callback'),

]