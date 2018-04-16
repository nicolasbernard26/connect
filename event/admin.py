from django.contrib import admin

from event.models.involvement import Involvement
from event.models.event import Event
from event.models.photoEvent import PhotoEvent


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


admin.site.register(Involvement, InvolvementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(PhotoEvent, PhotoEventAdmin)