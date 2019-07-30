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
    #followers = models.ManyToManyField(Profile, through='Follow')
    profiles_following = models.ManyToManyField('self', through='Follow', symmetrical=False)

    def __str__(self):
        return "{0}".format(self.user)

    def getName(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

class Follow(models.Model):

    followers = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, {1}".format(self.followers, self.following) 

    def getFollowing(self):
        return self.following

    def getFollower(self):
        return self.followers

