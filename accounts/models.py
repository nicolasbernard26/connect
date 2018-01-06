from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    """ 
    Profile : Description des utilisateurs.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")  # La liaison OneToOne vers le modèle User
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    background = models.ImageField(null=True, blank=True, upload_to="backgrounds/")
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.user)
