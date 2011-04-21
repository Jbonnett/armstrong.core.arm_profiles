from django.conf.urls.defaults import *
from armstrong.core.arm_profiles.views import (UserProfileDetailView,
        UserProfileUpdateView)


urlpatterns = patterns('',

    url(r'^update/$', UserProfileUpdateView.as_view(),
        name='profile_update'),

    url(r'^(?P<username>[\w.@+-]+)/$', UserProfileDetailView.as_view(),
        name='profile_detail'),

)
