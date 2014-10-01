from django.forms import ModelForm
from schools.models import School
import django_filters

class SchoolFilter(django_filters.FilterSet):
  class Meta:
      model = School
      fields = {'name': ['icontains'], 'address': ['icontains'],
                'school_type': ['exact'], 'garden': ['exact']
               }