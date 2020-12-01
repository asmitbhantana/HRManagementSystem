"""HRManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from Dashboard.urls import index
from Dashboard.views.views import base

urlpatterns = [
                  path('base/', base),
                  path('admin/', admin.site.urls),
                  path('user/', include('Account.urls'), name='user'),
                  path('dashboard/', include('Dashboard.urls'), name="dashboard"),
                  path('jobs/', include('Job.urls'), name="jobs"),

                  path('', index, name="index"),
                  path('vacancy/', include('Vacancy.urls'), name="vacancy"),
                  path('exam/', include('Exam.urls'), name="exam"),

                  path('question/', include('Question.urls'), name="question"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
