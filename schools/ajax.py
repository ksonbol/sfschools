from schools.forms import SchoolForm, SchoolFilter
from django.core import serializers
import json, pdb

# @dajaxice_register(method="GET")
# def filter(request):
#     f = SchoolFilter(request.GET)
#     # pdb.set_trace()
#     return serializers.serialize("json", f)
