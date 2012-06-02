from django.db import models
from schools.models import School


class Event(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
