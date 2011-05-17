from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from idios.views import ProfileDetailView


class ActiveProfileDetailView(ProfileDetailView):
    
    def get_object(self):
        obj = super(ActiveProfileDetailView, self).get_object()
        if obj.user.is_active:
            return obj
        else:
            raise Http404
