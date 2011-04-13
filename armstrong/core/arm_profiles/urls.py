from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns += patterns('',
    url(r'^profiles/(?P<profile_slug>.*)$', 'arm_profiles.views.profiles_detail', name='profiles_detail'),
)
