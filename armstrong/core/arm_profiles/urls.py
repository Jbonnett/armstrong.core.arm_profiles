from django.conf.urls.defaults import *
from django.views.generic.create_update import update_object
from django.shortcuts import get_object_or_404
from armstrong.core.arm_profiles.models import UserProfile
from armstrong.core.arm_profiles.views import (UserProfileDetailView,
        UserProfileUpdateView)


urlpatterns = patterns('',

    url(r'^update/$', UserProfileUpdateView.as_view(),
        name='profile_update'),

    url(r'^(?P<username>[\w.@+-]+)/$', UserProfileDetailView.as_view(),
        name='profile_detail'),

)
