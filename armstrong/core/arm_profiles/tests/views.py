from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from ..models import UserProfile
from ._utils import TestCase

class ProfileViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('otis',
            'otis@armstrongcms.org', 'pw')

        profile = self.user.get_profile()
        profile.location = "sittin' on the dock of the bay"
        profile.about = "american soooul singer"
        profile.save()

        self.c = Client()
        self.assertEqual(self.c.login(username='otis', password='pw'), True)

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/profiles/profile/%s/'
                % self.user.username)

    def test_detail_view(self):
        response = self.c.get(self.user.get_absolute_url())
        self.assertEqual(self.user.get_profile(), response.context['profile'])

    def test_no_profile_found(self):
        response = self.c.get(reverse('profile_detail',
                kwargs={'username':'crocker'}))
        self.assertEqual(response.status_code, 404)

    def test_non_public_profile(self):
        self.user.get_profile().public = False
        self.user.get_profile().save()
        response = self.c.get(self.user.get_absolute_url())
        self.assertNotContains(response, self.user.email)

    def test_non_active_profile(self):
        self.user.is_active = False
        self.user.save()
        response = self.c.get(self.user.get_absolute_url())
        self.assertEqual(response.status_code, 404)
