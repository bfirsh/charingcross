from django.conf import settings
from django.views.generic import TemplateView
from charingcross.utils import github_from_request

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        gh = github_from_request(self.request)
        #context['repos'] = gh.get_organization(settings.SOCIAL_AUTH_GITHUB_ORG_NAME).get_repos('all')
        context['repos'] = gh.get_user().get_repos()
        return context
