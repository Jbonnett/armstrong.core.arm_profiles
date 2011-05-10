from django.db import models

class UserProfileManager(models.Manager):

    def get_query_set(self):

        return super(UserProfileManager, self).get_query_set().filter(
                user__is_active=True)
