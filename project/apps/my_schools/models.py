from django.db import models
from schools.models import School

class Person(models.Model):
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return "Facebook user: %s" % self.facebook_id

class PersonSchool(models.Model):
    school = models.ForeignKey(School)

    def __unicode__(self):
        return "%s" % self.school