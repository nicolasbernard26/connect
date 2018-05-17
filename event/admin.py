from django.contrib import admin

from event.models.involvement_model import InvolvementModel
from event.models.event_model import EventModel
from event.models.photo_event_model import PhotoEventModel


class EventAdmin(admin.ModelAdmin):
    list_display   = ('title', 'admin', 'theme', 'date_start')
    date_hierarchy = 'date_start'
    ordering       = ('date_start', )
    search_fields  = ('title', 'theme', 'description')


class InvolvementAdmin(admin.ModelAdmin):
    list_display   = ('event', 'profile')
    search_fields  = ('event', 'profile')


class PhotoEventAdmin(admin.ModelAdmin):
    list_display   = ('event', 'photo')
    search_fields  = ('event', 'photo')


admin.site.register(InvolvementModel, InvolvementAdmin)
admin.site.register(EventModel, EventAdmin)
admin.site.register(PhotoEventModel, PhotoEventAdmin)