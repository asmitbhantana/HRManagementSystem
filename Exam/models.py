from django.db import models

from Question.models import Question
from Job.models import Jobs, Application


# Create your models here.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    choose_answer = models.CharField(null=False, blank=False, max_length=1)
    for_application = models.ForeignKey(Application, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.for_application.applicant.username + "--for--" + self.for_application.job.title
