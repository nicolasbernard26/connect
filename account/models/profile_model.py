from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    """
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    background = models.ImageField(null=True, blank=True, upload_to="backgrounds/")
    inscrit_newsletter = models.BooleanField(default=False)
<<<<<<< HEAD:accounts/models.py
    #followers = models.ManyToManyField(Profile, through='Follow')
    profiles_following = models.ManyToManyField('self', through='Follow', symmetrical=False)
=======
    connections = models.ManyToManyField('self', symmetrical=True)
>>>>>>> 9f2c1ce7f3118310e93bcf24a89c451064f86846:account/models/profile_model.py

    def __str__(self):
        return "{0}".format(self.user)

    def getName(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

<<<<<<< HEAD:accounts/models.py
class Follow(models.Model):

    followers = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, {1}".format(self.followers, self.following) 

    def getFollowing(self):
        return self.following

    def getFollower(self):
        return self.followers

=======
    def get_involvement(self):
        return self.involves.all()
>>>>>>> 9f2c1ce7f3118310e93bcf24a89c451064f86846:account/models/profile_model.py
