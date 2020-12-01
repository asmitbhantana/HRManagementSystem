from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from Job.models import Jobs, Application
from Question.models import Question
from Exam.models import Answer


# Create your views here.


@login_required
def give_exam(request, job_id):
    job = Jobs.objects.get(id=job_id)
    title = job.title
    position = job.required_position
    questions = Question.objects.filter(job_id=job.id)
    return render(request, 'Exam/take-exam.html',
                  {'title': title,
                   'position': position,
                   'question_list': questions,
                   'job_id': job_id,
                   'total_question': len(questions)})


def submit_exam(request):
    if request.method == "POST" and request.is_ajax():
        current_user = request.user
        print("GET is", request.POST)
        answers = list(request.POST.get("submitted"))
        questions = list(request.POST.get("question"))
        job_id = list(request.POST.get("job_id"))
        job_id = job_id[0]

        print("Answers are", answers)
        print("Questions are", questions)
        print("Job", job_id)

        total_questions = len(Question.objects.filter(job_id=job_id))

        application = Application.objects.get(applicant=request.user, job_id=job_id)

        correct_answers = 0
        if application.exam_attended:
            return JsonResponse({"message": "unsuccessful"}, status=404)

        for index in range(len(answers)):
            try:
                int(answers[index])
                answer = Answer()

                question = Question.objects.get(pk=questions[index])
                answer.question = question
                answer.choose_answer = answers[index]

                if question.correct_option == answers[index]:
                    correct_answers += 1

                answer.for_application = application
                answer.save()
            except ValueError:
                print("Error occured")

        application.obtained_marks = f"{correct_answers}/{total_questions}"
        application.exam_attended = True
        application.save()

        return JsonResponse({"message": "success"}, status=200)
