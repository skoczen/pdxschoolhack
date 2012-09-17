from django.db import models
from schools.models import School
from django_facebook.models import FacebookProfileModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Person(FacebookProfileModel):
    user = models.OneToOneField('auth.User')

    @property
    def schools(self):
        return [s.school for s in self.personschool_set.all()]

class PersonSchool(models.Model):
    person = models.ForeignKey(Person)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return "%s" % self.school



def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)
