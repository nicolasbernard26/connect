from django.conf.urls import url
from event_API.views.entry_view import EntryView
from event_API.views.event_view import EventView
from event_API.views.photo_view import PhotoView

urlpatterns = [
    #url(r'^$', EventView.as_view(), name="event"),
    url(r'^(?P<id_event>\d+)$', EventView.as_view(), name="event"),
    url(r'^(\d+)/photo$', PhotoView.as_view(), name="event"),
    url(r'^(\d+)/entries$', EntryView.as_view(), name="event"),
]