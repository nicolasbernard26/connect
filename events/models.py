#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
 
"""
    Ceci est un module génial qui va faire 
    plein de trucs super cool.
"""

from django.db import models
from PIL import Image

from accounts.models import Profile
from events.choices.themes_event import *


def file_path(instance, filename):
    file_path_photo = 'events/event_{event_id}/{name}'.format(
         event_id = instance.event.id, name = filename) 
    return file_path_photo

def file_path_event_photo(instance, filename):
    file_path_photo = 'events/event_{event_id}/main_{name}'.format(
         event_id = instance.id, name = filename) 
    return file_path_photo


class Event(models.Model):
    """
    \tModel for event :
        title : CharField,
        admin : Profile,
        place : CharField,
        description : TextField,
        date_start : DateTimeField,
        date_end : DateTimeField,
        entries : ManyToMany(Profile),
        theme : IntergerField.
    """
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(Profile, related_name='creator', on_delete=models.CASCADE)
    place = models.CharField(max_length=42)
    description = models.TextField(null=True)
    date_start = models.DateTimeField(auto_now_add=False, auto_now=False)
    date_end = models.DateTimeField(auto_now_add=False, auto_now=False)
    entries = models.ManyToManyField(Profile, through='Involvement')
    theme = models.IntegerField(choices=THEMES_CHOICES, default=5)
    photo_event = models.ImageField(null=True, blank=True, upload_to=file_path_event_photo)

    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.title

    def getAdmin(self):
        return "{0} {1}".format(self.admin, self.admin)

class Involvement(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="involve")

    def __str__(self):
        return "{0}, {1}".format(self.profile, self.event)

    class Meta:
        unique_together = ('event', 'profile',)


class PhotoEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(null=True, blank=True, upload_to=file_path)
    owner = models.ForeignKey(Profile, related_name='own_photo', on_delete=models.CASCADE, default=13)
    title = models.CharField(max_length=100, default="")


    def __str__(self):
        return "{0}, {1}, {2}".format(self.event, self.photo, self.owner)

