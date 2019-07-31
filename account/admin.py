from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
from account.models.notification_model import NotificationModel
from account.models.profile_model import ProfileModel

TokenAdmin.raw_id_fields = ('user',)


admin.site.register(ProfileModel)
admin.site.register(NotificationModel)
