# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

# Create your models here.
class Account(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    whatsapp = models.CharField(max_length=15)

    def __unicode__(self):
        full_name = self.user.first_name + " " + self.user.last_name
        return full_name

    def __str__(self):
        full_name = self.user.first_name + " " + self.user.last_name
        return full_name

    class Meta:
        verbose_name_plural = "Accounts"


class RecoverAccount(models.Model):

    STATUS_C = (
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('E', 'Error'),
    )

    account = models.ForeignKey(Account)
    email = models.EmailField()
    token = models.CharField(max_length=256)
    status = models.CharField(max_length=11, choices=STATUS_C, default='P')
    created = models.DateTimeField(auto_now_add=True)
    token_used = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Recover Tokens"