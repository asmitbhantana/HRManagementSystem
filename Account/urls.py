from django.urls import path

from .views import UserLogoutView, UserSignupView, UserLoginView

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', UserSignupView.as_view(), name="register"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
