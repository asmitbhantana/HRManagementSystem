from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from Job.models import Jobs
from .models import Question
from .forms import QuestionCreateForm


# Create your views here.
class ListQuestionsView(ListView):
    model = Question
    template_name = 'Question/list-question.html'

    def get_queryset(self):
        return Question.objects.filter(job_id=self.kwargs.get('job_id', None))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_job_id'] = self.kwargs.get('job_id', None)
        return context


class CreateQuestionsView(FormView):
    model = Question
    template_name = 'Question/add-question.html'
    form_class = QuestionCreateForm

    def form_valid(self, form):
        question = form.save(commit=False)
        job_id = self.kwargs.get('job_id', None)
        question.job = Jobs.objects.get(id=job_id)
        if job_id:
            self.success_url = reverse_lazy('questions:list', kwargs={'job_id': job_id})
        question.save()
        return super().form_valid(form)


class DeleteQuestionView(DeleteView):
    model = Question

    def get_queryset(self):
        job_id = self.kwargs.get('job_id', None)
        if job_id:
            return Question.objects.filter(job_id=job_id)
        return None

    def get(self, request, *args, **kwargs):
        job_id = self.kwargs.get('job_id', None)
        if job_id:
            self.success_url = reverse_lazy('questions:list', kwargs={'job_id': job_id})
        return self.post(request, *args, **kwargs)


class UpdateQuestionView(UpdateView):
    template_name = 'Question/edit-question.html'
    form_class = QuestionCreateForm
    model = Question

    def form_valid(self, form):
        question = form.save(commit=False)
        job_id = self.kwargs.get('job_id', None)
        question.job = Jobs.objects.get(id=job_id)
        if job_id:
            self.success_url = reverse_lazy('questions:list', kwargs={'job_id': job_id})
        question.save()
        return super().form_valid(form)
