"""
high level support for doing this and that.
"""
from django.conf.urls import url
from .views import sign_up_view, login_view, logout_view, index, my_profile_view

urlpatterns = [
    url(r'^sign-up/$', sign_up_view),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', index, name='index'),
    url(r'^profile/$', my_profile_view, name='profile'),
]
