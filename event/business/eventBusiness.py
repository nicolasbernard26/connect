from account.models.profile_model import Profile
from event.models.event import Event
from django.core.files.images import ImageFile


class EventBusiness:
    """
    Contains all the business function for Event.
    """

    def __init__(self, event: Event):
        self.__event = event

    def __init__(self, form, profile, photo):
        self.__event = Event(
            title=form.get("title"),
            admin=profile,
            place=form.get("place"),
            description=form.get("description"),
            date_start=form.get("date_end"),
            date_end=form.get("date_end"),
            photo_event=ImageFile(photo)
        )

    def get_all_photos(self):
        return self.__event.photos.all()

    def get_event(self):
        return self.__event

    def save(self):
        self.__event.save()
