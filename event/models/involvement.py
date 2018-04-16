#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Ceci est un module génial qui va faire
    plein de trucs super cool.
"""

from django.db import models
from account.models.profile_model import Profile
from event.models.event import Event


class Involvement(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="involves")

    def __str__(self):
        return "{0}, {1}".format(self.profile, self.event)

    class Meta:
        unique_together = ('event', 'profile')
