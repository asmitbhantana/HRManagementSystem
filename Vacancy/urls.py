from django.urls import path
from .views import ApplyJobView, select_for_exam

app_name = "vacancy"
urlpatterns = [
    path('apply/<int:pk>', ApplyJobView.as_view(), name="apply"),
    path('interview/<int:application_id>', select_for_exam, name="exam"),
]
