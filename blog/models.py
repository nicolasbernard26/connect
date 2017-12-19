from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    admin = models.CharField(max_length=42)
    place = models.CharField(max_length=42)
    description = models.TextField(null=True)
    date_start = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_end = models.DateTimeField(auto_now_add=False, auto_now=False)
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.title

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user)