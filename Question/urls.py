from django.urls import path
from .views import ListQuestionsView, CreateQuestionsView, DeleteQuestionView, UpdateQuestionView

app_name = "questions"
urlpatterns = [
    path('list/<int:job_id>', ListQuestionsView.as_view(), name='list'),
    path('create/<int:job_id>', CreateQuestionsView.as_view(), name='create'),
    path('delete/<int:pk>/<int:job_id>/', DeleteQuestionView.as_view(), name='delete'),
    path('update/<int:pk>/<int:job_id>/', UpdateQuestionView.as_view(), name='update'),
]
