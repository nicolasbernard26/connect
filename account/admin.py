from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
from account.models.profile_model import Profile

TokenAdmin.raw_id_fields = ('user',)


admin.site.register(Profile)