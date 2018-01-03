"""
high level support for doing this and that.
"""
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^event/detail/(\d+)$', views.detail)
]

urlpatterns += staticfiles_urlpatterns()
