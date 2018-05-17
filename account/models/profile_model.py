from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    """
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    background = models.ImageField(null=True, blank=True, upload_to="backgrounds/")
    inscrit_newsletter = models.BooleanField(default=False)
    connections = models.ManyToManyField('self', symmetrical=True)

    def __str__(self):
        return "{0}".format(self.user)

    def getName(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    def get_involvement(self):
        return self.involves.all()
