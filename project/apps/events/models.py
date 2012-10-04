from django.db import models
from schools.models import School
# from open_facebook.api import *


class Event(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to="uploads/events")
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True, editable=False)

    def __unicode__(self):
        return "%s" % self.name

    @property
    def facebook_event_url(self):
        return "https://www.facebook.com/events/%s/" % self.facebook_id

    class Meta:
        ordering = ("start_time",)

    def create_facebook_event(self):
        raise Exception("Not yet implemented")
        # if not self.facebook_id:
        # fb = OpenFacebook.
        # https://developers.facebook.com/docs/reference/api/page/#page_access_tokens
        # https://github.com/tschellenbach/Django-facebook/blob/master/open_facebook/api.py
