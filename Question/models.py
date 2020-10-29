from django.db import models

from Job.models import Jobs


# Create your models here.
class Question(models.Model):
    question = models.TextField(unique=True)
    option_1 = models.CharField(max_length=100, blank=False, null=False)
    option_2 = models.CharField(max_length=100, blank=False, null=False)
    option_3 = models.CharField(max_length=100, blank=False, null=False)
    option_4 = models.CharField(max_length=100, blank=False, null=False)

    options = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4'),
    ]
    correct_option = models.CharField(
        max_length=1,
        choices=options,
        default='1',
    )

    job = models.ForeignKey(Jobs, on_delete=models.SET_DEFAULT, default=8)

    def __str__(self):
        return self.question + " -->" + self.job.title
