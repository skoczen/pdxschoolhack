import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class SchoolType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s" % self.name

class School(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, editable=False)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    school_type = models.ForeignKey(SchoolType)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.name

    def permalink(self):
        return reverse("schools:detail", args=(self.slug,))

    def upcoming_events(self):
        now = datetime.datetime.now()
        return self.event_set.all().filter(end_time__gte=now)[:10]

    @property
    def map_querystring(self):
        s = "%(name)s,%(address)s,%(city)s, OR %(zip_code)s" % self.__dict__
        s.replace(" ", "+")
        return s