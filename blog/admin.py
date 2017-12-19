from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display   = ('title', 'admin', 'date_start')
    date_hierarchy = 'date_start'
    ordering       = ('date_start', )
    search_fields  = ('title', 'description')

admin.site.register(Event, EventAdmin)
