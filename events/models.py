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

    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.title

    def getAdmin(self):
        return "{0} {1}".format(self.admin.user.first_name, self.admin.user.last_name)

class Involvement(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, {1}".format(self.profile, self.event)

class PhotoEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to=file_path)
    orientation = models.BooleanField(default=False)
    title = models.CharField(max_length=100, default="")


    def __str__(self):
        return "{0}, {1}".format(self.event, self.photo)

    def getOrientation(self):
        img = Image.open(self.photo).rotate(90, expand=True)
        print(img)
        self.orientation = True
        return True

