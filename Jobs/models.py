from django.db import models
from django.contrib.auth import get_user_model

from User.models import SystemUser


class Jobs(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    team_lead = models.OneToOneField(SystemUser, on_delete=models.SET_NULL)
    required_position = models.CharField(max_length=100, blank=False, null=False)


class Application(models.Model):
    User = get_user_model()
    job = models.OneToOneField(Jobs, on_delete=models.SET_NULL, null=True, blank=False)
    applicants = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="applicant")
    team_lead = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="team_lead")
    cv = models.FileField(upload_to="\media\cv", null=False, blank=False)
