from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField()

    about = models.TextField(null=True, blank=True)
    photo = ImageField()
    website = models.URLField(null=True, blank=True, verify_exists=False)

    facebook_name = models.CharField(max_length=100, blank=True)
    twitter_name = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(max_length=100, verify_exists=False,
        blank=True, null=True)

    show_email = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'profile_slug': self.slug})
