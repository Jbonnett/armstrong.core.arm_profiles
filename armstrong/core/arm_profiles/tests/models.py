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

        profile = self.user.get_profile()
        profile.location = "sittin' on the dock of the bay"
        profile.about = "american soooul singer"
        profile.save()

        self.user2 = User.objects.create_user('paolo',
            'paolo@armstrongcms.org', 'pwrd')

        self.c = Client()
        self.assertEqual(self.c.login(username='otis', password='pw'), True)

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/profiles/profile/%s/' % self.user.username)

    def test_detail_view(self):
        response = self.c.get(self.user.get_absolute_url())
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_get_edit_form(self):
        response = self.c.get(reverse('profile_edit'))
        self.assertTrue('profile_form' in response.context)

    def test_deny_edit_form(self):
        self.c.logout()
        response = self.c.get(reverse('profile_edit'))
        self.assertRedirects(response, '%s?next=%s' % (getattr(settings, 'LOGIN_URL'), reverse('profile_edit')))

    def test_no_profile_found(self):
        response = self.c.get(reverse('profile_detail', kwargs={'username':'crocker'}))
        self.assertEqual(response.status_code, 404)

    def test_non_public_profile(self):
        self.user2.get_profile().public = False
        self.user2.get_profile().save()
        response = self.c.get(self.user2.get_absolute_url())
        self.assertNotContains(response, self.user2.email)

    def test_non_active_profile(self):
        self.user2.is_active = False
        self.user2.save()
        response = self.c.get(self.user2.get_absolute_url())
        self.assertEqual(response.status_code, 404)
