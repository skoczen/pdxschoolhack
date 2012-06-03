from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class SchoolType(models.Model):
    name = models.CharField(max_length=255)


class School(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    lat = models.IntegerField()
    lon = models.IntegerField()
    school_type = models.ForeignKey(SchoolType)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)
