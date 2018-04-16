from account.models.profile_model import Profile
from event.business.eventBusiness import EventBusiness
from account.business.profile_business import ProfileBusiness
from event.models.involvement import Involvement


class InvolvementBusiness:

    """
    Contains all the business function for Event.
    """

    def __init__(self, profile: Profile, id_event: int):
        involve = profile.get_involvement().filter(id=id_event)
        self.__hasRight = involve.count() == 1
        if self.__hasRight:
            self.__eventBusiness = EventBusiness(involve[0].event)
            self.__profileBusiness = ProfileBusiness(involve[0].profile)

    def get_event_business(self):
        return self.__eventBusiness

    def get_profile_business(self):
        return self.__profileBusiness

    def has_right(self):
        return self.__hasRight
