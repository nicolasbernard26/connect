from django.http import QueryDict

from account.constant.choices.notification_types import NOTIFICATION_TYPES
from account.models.notification_model import NotificationModel
from account.repository.profile_repository import ProfileRepository
from connect.shared.base_repository import BaseRepository
from django.utils import timezone
import pytz


class NotificationRepository(BaseRepository):

    @staticmethod
    def get_by_id(id: int):
        return NotificationModel.objects.get(id=id)

    @staticmethod
    def create(
            id_profile: int,
            id_profile_related: int,
            notification_type: NOTIFICATION_TYPES,
            object=None) -> NotificationModel:

        profile = ProfileRepository().get_by_id(id_profile)
        profile_related = ProfileRepository().get_by_id(id_profile_related)

        if object:
            return NotificationModel(profile=profile,
                                     type=notification_type,
                                     profileRelated=profile_related,
                                     object=object,
                                     dateCreated=timezone.now(),
                                     dateRemoved=timezone.now())
        else:
            return NotificationModel(profile=profile,
                                     type=notification_type,
                                     profileRelated=profile_related,
                                     dateCreated=timezone.now(),
                                     dateRemoved=timezone.now())

    @staticmethod
    def save(notification: NotificationModel):
        notification.save()
