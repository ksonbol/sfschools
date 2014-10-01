from django.db import models
from django.db.models.query import QuerySet
from django.core.urlresolvers import reverse

class SchoolsMixin(object):
    def by_school_type(self, school_type):
        return self.filter(school_type=school_type)

    def by_address(self, address):
        return self.filter(address=address)

class SchoolQuerySet(QuerySet, SchoolsMixin):
    pass

class SchoolManager(models.Manager, SchoolsMixin):
    def get_queryset(self):
        return SchoolQuerySet(self.model, using=self._db)

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    school_type = models.CharField(max_length=255, blank=True)
    garden = models.NullBooleanField()
    enroll_cnt = models.IntegerField(null=True, blank=True)
    objects = SchoolManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schools:list')