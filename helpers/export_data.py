from __future__ import absolute_import
import os
from helpers import dbf_handler
from django.conf import settings

def export_schools(file_name):
  with open(file_name, 'rb') as f:
    contents = dbf_handler.dbfreader(f)
    i = 0
    # field_names = contents[0]
    # field_specs = contents[1]
    for row in contents:
      i += 1
      if i < 3:
        continue
      name = row[0].strip()
      address = row[1].strip()
      garden = row[3].strip()
      if garden == 'yes':
        garden = True
      elif garden == 'no':
        garden = False
      else:
        garden = None
      school_type = row[4].strip()
      enroll_cnt = row[14]
      if type(enroll_cnt) == str:
        enroll_cnt = enroll_cnt.strip()
      enroll_cnt = int(enroll_cnt)
      School.objects.create(name=name, address=address, garden=garden,
        school_type=school_type, enroll_cnt=enroll_cnt)

# file_name = os.path.join(settings.BASE_DIR, 'data', 'SanFranciscoPublicSchools.dbf')
# export_schools(file_name)