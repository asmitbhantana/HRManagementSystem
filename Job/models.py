from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

from User.models import SystemUser

User = get_user_model()


class Jobs(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    team_lead = models.ForeignKey(SystemUser, on_delete=models.SET_DEFAULT, default=1, blank=False)
    required_position = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.SET_DEFAULT, null=True, blank=False, default=0)
    applicant = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=False, blank=False, related_name="applicant",
                                  default=1)
    cv = models.FileField(upload_to="\media\cv", null=False, blank=False)
    selected_for_exam = models.BooleanField(default=False)

    def __str__(self):
        return self.job.title + " by " + self.applicant.username
