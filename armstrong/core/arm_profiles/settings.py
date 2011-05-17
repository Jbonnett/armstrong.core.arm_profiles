from django.conf import settings

PHOTO_PATH = getattr(settings, 'ARMSTRONG_PROFILES_PHOTO_PATH',
        'arm_profiles/photos')
