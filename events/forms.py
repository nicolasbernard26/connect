from django import forms
from .models import Event, Involvement

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','description', 'place', 'date_start', 'date_end', 'theme', 'photo_event',)


class InvolvementForm(forms.ModelForm):
    class Meta:
        model = Involvement
        fields = ('profile',)

        from django import forms



class MyCustomForm(forms.Form):
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('my_choices')
       super(MyCustomForm, self).__init__(*args, **kwargs)
       self.fields["other_field"] = forms.ChoiceField(choices=choices)
   
    other_field = forms.ChoiceField()