from django.db import models
from django.core.urlresolvers import reverse

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    school_type = models.CharField(max_length=255, blank=True)
    garden = models.NullBooleanField()
    enroll_cnt = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schools:list')