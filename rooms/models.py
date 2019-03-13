# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from locations.models import State, City
from accounts.models import Account

# Create your models here.
class Room(models.Model):

    GENDER_C = (
        ('M', 'Somente Homens'),
        ('F', 'Somente Mulheres'),
        ('ND', 'Homens/Mulheres'),
    )

    BUILD_C = (
        ('apto', 'Apartamento'),
        ('house', 'Casa'),
        ('pens', 'Pensionato'),
        ('hostel', 'Hostel'),
        ('rep', 'República'),
    )

    TYPE_C = (
        ('one', 'Individual'),
        ('many', 'Coletivo'),
        ('couple', 'Casal'),
    )

    BATH_C = (
        ('priv', 'Individual/Privativo'),
        ('col', 'Coletivo'),
        ('split', 'Compartilhado para Dois'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    building = models.CharField(max_length=8, choices=BUILD_C, default='apto')
    type = models.CharField(max_length=8, choices=TYPE_C, default='one')
    bathroom = models.CharField(max_length=8, choices=BATH_C, default='priv')
    gender = models.CharField(max_length=3, choices=GENDER_C, default='ND')
    description = models.TextField(max_length=400, default="")
    smoking = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    include_bills = models.BooleanField(default=False)
    visits = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    furniture = models.BooleanField(default=False)
    value = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(2000)])
    active = models.BooleanField(default=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.CharField(max_length=20, default='')
    cep = models.CharField(max_length=12, null=True, blank=True, default='')
    contact_name = models.CharField(max_length=30, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_full_location(self):
        location = self.city.name + "-" + self.state.code
        return location

    def get_gender(self):
        for value in self.GENDER_C:
            if value[0] == self.gender:
                return value[1]

    def get_build(self):
        for value in self.BUILD_C:
            if value[0] == self.building:
                return value[1]

    def get_type(self):
        for value in self.TYPE_C:
            if value[0] == self.type:
                return value[1]

    def get_bath(self):
        for value in self.BATH_C:
            if value[0] == self.bathroom:
                return value[1]

    def get_bool_field(self, field):
        value = self.__getattribute__(field)
        if value:
            return "Sim"
        else:
            return "Não"

    def active_toogle(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    class Meta:
        verbose_name_plural = "Rooms"