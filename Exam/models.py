from django.db import models

from Question.models import Question
from Job.models import Jobs, Application


# Create your models here.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    options = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4'),
    ]
    choose_answer = models.CharField(
        max_length=1,
        choices=options,
    )
    for_application = models.ForeignKey(Application, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.for_application.applicant.username + "--for--"+self.for_application.job.title