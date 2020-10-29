from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import FormView
from Job.models import Jobs, Application
from Question.models import Question
from Exam.models import Answer


# Create your views here.
class CreateQuestion(FormView):
    pass


@login_required
def give_exam(request, job_id):
    job = Jobs.objects.get(id=job_id)
    title = job.title
    position = job.required_position
    questions = Question.objects.filter(job_id=job.id)
    return render(request, 'Exam/take-exam.html', {'title': title, 'position': position, 'question': questions})
