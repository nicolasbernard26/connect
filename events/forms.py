from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','description', 'place', 'date_start', 'date_end', 'theme', 'photo_event',)