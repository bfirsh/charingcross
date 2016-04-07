"""charingcross URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from charingcross.home.views import HomeView
from charingcross.repos.views import RepoView

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(HomeView.as_view())),
    url(r'^repos/(?P<full_name>[^/]+/[^/]+)$', login_required(RepoView.as_view()), name="repo"),
    url(r'^login$', TemplateView.as_view(template_name="login.html")),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
]
