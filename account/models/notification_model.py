#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Ceci est un module génial qui va faire
    plein de trucs super cool.
"""

from django.db import models
from account.models.profile_model import ProfileModel
from event.models.event_model import EventModel
from event.models.photo_event_model import PhotoEventModel
from account.constant.choices.notification_types import NOTIFICATION_TYPES
from datetime import datetime


class NotificationModel(models.Model):
    profile = models.ForeignKey(ProfileModel, related_name='notifications', on_delete=models.DO_NOTHING)
    type = models.IntegerField(choices=NOTIFICATION_TYPES, default=4)
    profileRelated = models.ForeignKey(ProfileModel, on_delete=models.DO_NOTHING, blank=True, null=True)
    eventRelated = models.ForeignKey(EventModel, on_delete=models.DO_NOTHING, blank=True, null=True)
    photoEventRelated = models.ForeignKey(PhotoEventModel, on_delete=models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=300, blank=True)

    dateCreated = models.DateTimeField(default=datetime.now, blank=True)
    dateRemoved = models.DateTimeField(default=datetime.now, blank=True)
    delete = models.BooleanField(default=False)
    see = models.BooleanField(default=False)

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.profile, self.object, self.type, self.message)

    @property
    def object(self):
        return self.profileRelated or self.eventRelated or self.photoEventRelated

    @object.setter
    def object(self, obj):
        if type(obj) == ProfileModel:
            self.profileRelated = obj
            self.eventRelated = None
            self.photoEventRelated = None
        elif type(obj) == EventModel:
            self.profileRelated = None
            self.eventRelated = obj
            self.photoEventRelated = None
        elif type(obj) == PhotoEventModel:
            self.profileRelated = None
            self.eventRelated = None
            self.photoEventRelated = obj
        else:
            raise ValueError("obj parameter must be an object of Business or Person class")
