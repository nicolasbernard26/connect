from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views import profile, login, connections, events

urlpatterns = [
    url(r'^profile/(\d+)$', profile, name="profile"),
    url(r'^login/$', login, name="login"),
    url(r'^connections/$', connections, name="connections"),
    url(r'^events/$', events, name="events")
]