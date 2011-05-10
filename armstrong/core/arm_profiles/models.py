from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from idios.models import ProfileBase
from armstrong.core.arm_profiles.managers import UserProfileManager


class UserProfile(ProfileBase):

    public = models.BooleanField(default=True)
    location = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    website = models.URLField(blank=True, verify_exists=False)
    photo = ImageField(upload_to=getattr(settings,
            'ARM_PROFILES_PHOTO_PATH', 'arm_profiles/photos'))

    objects = UserProfileManager()

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
