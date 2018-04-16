from event.business.involvementBusiness import InvolvementBusiness
from event.models.photoEvent import PhotoEvent
from event.business.eventBusiness import EventBusiness
from account.business.profile_business import ProfileBusiness
from django.core.files.images import ImageFile


class PhotoEventBusiness:

    """
    Contains all the business function for Event.
    """

    def __init__(self, photo, event: EventBusiness, profile: ProfileBusiness, title):
        self.__photo = PhotoEvent(
            photo=ImageFile(photo),
            event=event.get_event(),
            owner=profile.get_profile(),
            title=title
        )

    def get_photo(self):
        return self.__photo

    def save(self):
        self.__photo.save()
