from django.forms import ModelForm
from armstrong.core.arm_profiles.models import UserProfile

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
