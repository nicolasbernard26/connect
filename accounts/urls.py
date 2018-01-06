"""
high level support for doing this and that.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sign-up/$', views.sign_up_view),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile_view),
]
