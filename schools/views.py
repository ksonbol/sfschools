from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from schools.models import School
from schools.forms import SchoolForm, SchoolFilter
from django.views.generic.list import MultipleObjectMixin
import json

# Create your views here.
class SchoolListView(ListView):
    model = School
    paginate_by = 10

class SchoolFilterView(View, MultipleObjectMixin):
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        f = SchoolFilter(request.GET)
        return render(request, 'schools/results.html', {'school_list': f})
