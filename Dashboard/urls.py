from django.urls import path

from Dashboard.views.views import index

app_name = "dashboard"
urlpatterns = [
    path('index/', index, name="index"),
]
