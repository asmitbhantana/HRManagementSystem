from django.urls import path
from HRManagement import settings
from django.conf.urls.static import static

from Dashboard.views.views import index

app_name = "dashboard"
urlpatterns = [
                  path('index/', index, name="index"),
              ]
