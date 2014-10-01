from django.conf.urls import patterns, include, url
from schools.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', SchoolListView.as_view(), name='list'),
    url(r'^filter$', SchoolFilterView.as_view(), name='filter'),
)
