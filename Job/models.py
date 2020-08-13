from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

from User.models import SystemUser

User = get_user_model()


class Jobs(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    team_lead = models.ManyToManyField(SystemUser, null=True)
    required_position = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.OneToOneField(Jobs, on_delete=models.SET_NULL, null=True, blank=False)
    applicant = models.ManyToManyField(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="applicant")
    team_lead = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="team_lead")
    cv = models.FileField(upload_to="\media\cv", null=False, blank=False)

    def __str__(self):
        return self.job.title
