from account.models.profile_model import Profile
from event.models.event import Event


class ProfileBusiness:

    """
    Contains all the business function for Event.
    """

    def __init__(self, profile: Profile):
        self.__profile = profile

    def get_profile(self):
        return self.__profile
