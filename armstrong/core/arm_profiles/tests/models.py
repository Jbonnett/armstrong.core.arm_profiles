from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings
from ._utils import TestCase
from ..models import UserProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('otis',
            'otis@armstrongcms.org', 'pw')
        self.profile = UserProfile.objects.create(user=self.user)
        self.profile.location = "sittin' on the dock of the bay"
        self.profile.about = "american soooul singer"

        self.user2 = User.objects.create_user('paolo',
            'paolo@armstrongcms.org', 'pwrd')
        self.profile2 = UserProfile.objects.create(user=self.user2)

        self.c = Client()
        self.assertEqual(self.c.login(username='otis', password='pw'), True)

    def test_get_absolute_url(self):
        self.assertEqual(self.profile.get_absolute_url(), '/profiles/%s/' % self.user.username)

    def test_detail_view(self):
        response = self.c.get(self.profile.get_absolute_url())
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_get_update_form(self):
        response = self.c.get(reverse('profile_update'))
        self.assertTrue('form' in response.context)

    def test_deny_update_form(self):
        self.c.logout()
        response = self.c.get(reverse('profile_update'))
        self.assertRedirects(response, getattr(settings, 'LOGIN_URL') + "?next=/profiles/update/")

    def test_no_profile_found(self):
        response = self.c.get('/profiles/crocker/')
        self.assertEqual(response.status_code, 404)

    def test_non_public_profile(self):
        self.profile2.public = False
        self.profile2.save()
        response = self.c.get(self.profile2.get_absolute_url())
        self.assertNotContains(response, self.user.email)

    def test_non_active_profile(self):
        self.profile2.active = False
        self.profile2.save()
        response = self.c.get(self.profile2.get_absolute_url())
        self.assertEqual(response.status_code, 404)
