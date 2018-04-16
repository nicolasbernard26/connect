from django.conf.urls import url
from event_rest.views import event, photos, entries, set_event_photo, delete_photo, create

urlpatterns = [
    url(r'^$', create, name="event"),
    url(r'^(\d+)/$', event, name="event"),
    url(r'^(\d+)/photos/$', photos, name="event"),
    url(r'^(\d+)/entries/$', entries, name="event"),
    url(r'^(\d+)/setEventPhoto/$', set_event_photo, name="event"),
    url(r'^(\d+)/photos/photo/', delete_photo, name="event")
]