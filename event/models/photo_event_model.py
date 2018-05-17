#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Ceci est un module génial qui va faire
    plein de trucs super cool.
"""

from django.db import models
from account.models.profile_model import ProfileModel
from event.models.event_model import EventModel


def file_path(instance, filename):
    file_path_photo = 'events/event_{event_id}/{name}'.format(
        event_id=instance.event.id, name=filename)
    return file_path_photo


class PhotoEventModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(null=True, blank=True, upload_to=file_path)
    owner = models.ForeignKey(ProfileModel, related_name='own_photos', on_delete=models.CASCADE, default=13)
    title = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return "{0}, {1}, {2}".format(self.event, self.photo, self.owner)

