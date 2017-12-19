"""
high level support for doing this and that.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_view),
    url(r'^logout$', views.logoutview, name='logout'),
    url(r'^$', views.index, name='index'),
]
