#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Ceci est un module génial qui va faire
    plein de trucs super cool.
"""

from django.db import models

from account.models.profile_model import ProfileModel
from event.choices.themes_event import THEMES_CHOICES


def file_path_event_photo(instance, filename):
    file_path_photo = 'events/event_{event_id}/main_{name}'.format(
        event_id=instance.id, name=filename)
    return file_path_photo


class EventModel(models.Model):
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
    admin = models.ForeignKey(ProfileModel, related_name='creator', on_delete=models.CASCADE)
    place = models.CharField(max_length=42)
    description = models.TextField(null=True)
    date_start = models.DateTimeField(auto_now_add=False, auto_now=False)
    date_end = models.DateTimeField(auto_now_add=False, auto_now=False)
    entries = models.ManyToManyField(ProfileModel, through='InvolvementModel')
    theme = models.IntegerField(choices=THEMES_CHOICES, default=5)
    photo_event = models.ImageField(null=True, blank=True, upload_to=file_path_event_photo)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title

    def get_admin(self):
        return "{0} {1}".format(self.admin, self.admin)
