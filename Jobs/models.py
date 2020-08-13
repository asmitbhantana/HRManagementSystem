from django.db import models

from User.models import SystemUser


class Jobs(models):
    title = models.CharField(max_length=150, blank=False, null=False)
    team_lead = models.OneToOneField(SystemUser, on_delete=models.SET_NULL)
    required_position = models.CharField(max_length=100, blank=False, null=False)


class Application(models):
    job = models.OneToOneField(Jobs, on_delete=models.SET_NULL, null=True, blank=False)
    applicants = models.OneToOneField(Jobs, on_delete=models.SET_NULL, null=True, blank=False)
    cv = models.FileField(upload_to="\media\cv", null=False, blank=False)
