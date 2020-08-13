from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from Job.models import Jobs, Application

class ApplyJobView(CreateView):
    model = Application




