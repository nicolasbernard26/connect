"""
high level support for doing this and that.
"""
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^event/detail/(\d+)$', views.detail),
    url(r'^event/create$', views.create),
    url(r'^event/add-participant/(\d+)$', views.add_participant)
]

urlpatterns += staticfiles_urlpatterns()
