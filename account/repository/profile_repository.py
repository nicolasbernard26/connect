from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.http import QueryDict

from account.models.profile_model import ProfileModel
from connect.errors.invalid_argument_error import InvalidArgumentError
from connect.shared.base_repository import BaseRepository


class ProfileRepository(BaseRepository):

    @staticmethod
    def get_by_id(id: int):
        return ProfileModel.objects.get(id=id)

    @staticmethod
    def check_password():
        return True

    @staticmethod
    def create(data: QueryDict, files: QueryDict):

        # region check parameter
        try:
            data.__getitem__("email")
        except InvalidArgumentError as err:
            print('Invalid argument error :', err)

        try:
            data.__getitem__("password")
        except InvalidArgumentError as err:
            print('Invalid argument error :', err)

        try:
            data.__getitem__("first_name")
        except InvalidArgumentError as err:
            print('Invalid argument error :', err)

        try:
            data.__getitem__("last_name")
        except InvalidArgumentError as err:
            print('Invalid argument error :', err)
        # endregion

        user: User = User.objects.create_user(data.__getitem__("email"),
                                              data.__getitem__("email"),
                                              data.__getitem__("password"))
        user.first_name = data.__getitem__("first_name")
        user.last_name = data.__getitem__("last_name")
        user.save()

        profile: ProfileModel = ProfileModel(user=user)
        for file_key in sorted(files):
            profile.avatar = ImageFile(files.FILES[file_key])
        return profile

    @staticmethod
    def save(profile: ProfileModel):
        profile.save()

    @staticmethod
    def get_by_id(id: int) -> ProfileModel:
        return ProfileModel.objects.get(id=id)
