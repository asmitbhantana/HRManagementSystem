from django.urls import path
from .views import give_exam

app_name = "exam"
urlpatterns = [
    path('<int:job_id>', give_exam, name="take"),

]
