from django.views.generic import DetailView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from armstrong.core.arm_profiles.models import UserProfile
from armstrong.core.arm_profiles.forms import UserProfileUpdateForm


class UserProfileDetailView(DetailView):

    model = UserProfile

    def get_object(self):
        return get_object_or_404(UserProfile,
            user__username=self.kwargs['username'], active=True)

class UserProfileUpdateView(UpdateView):

    form_class = UserProfileUpdateForm

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileUpdateView, self).dispatch(*args, **kwargs)
