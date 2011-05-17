from django.conf.urls.defaults import *
from armstrong.core.arm_profiles.views import ActiveProfileDetailView


urlpatterns = patterns('',

    url(r"^profile/(?P<username>[\w\._-]+)/$",
            ActiveProfileDetailView.as_view(), name="profile_detail"),
    url(r"^(?P<profile_slug>[\w\._-]+)/profile/(?P<profile_pk>\d+)/$",
            ActiveProfileDetailView.as_view(), name="profile_detail"),
    url(r"", include("idios.urls_base")),
    url(r"^(?P<profile_slug>[\w\._-]+)/", include("idios.urls_base")),

)
