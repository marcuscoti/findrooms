# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from locations.models import State, City
from accounts.models import Account

# Create your models here.
class Guest(models.Model):

    GENDER_C = (
        ('M', 'Homem'),
        ('F', 'Mulher'),
        ('ND', 'Não Informado'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=3, choices=GENDER_C, default='ND')
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    description = models.TextField(max_length=200, null=True, blank=True)
    work = models.BooleanField(default=False)
    study = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    max_value = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(2000)])
    active = models.BooleanField(default=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Guests"
