from django.urls import path
app_name = 'user'

from .views import UserLogoutView, UserSignupView, UserLoginView

url_patterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', UserSignupView.as_view(), name="register"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]