#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Ceci est un module génial qui va faire
    plein de trucs super cool.
"""

from django.db import models
from account.models.profile_model import ProfileModel
from event.models.event_model import EventModel


class InvolvementModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.DO_NOTHING, related_name="participants")
    profile = models.ForeignKey(ProfileModel, on_delete=models.DO_NOTHING, related_name="involves")

    def __str__(self):
        return "{0}, {1}".format(self.profile, self.event)

    class Meta:
        unique_together = ('event', 'profile')
