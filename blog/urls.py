"""
high level support for doing this and that.
"""
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^accueil$', views.home),
]

urlpatterns += staticfiles_urlpatterns()
