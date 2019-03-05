# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class State(models.Model):

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "States"


class City(models.Model):

    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        full_name = self.name + "-" + self.state.code
        return full_name

    def __str__(self):
        full_name = self.name + "-" + self.state.code
        return full_name

    class Meta:
        verbose_name_plural = "Cities"