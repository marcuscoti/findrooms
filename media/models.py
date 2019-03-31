# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.


class PictureManager(models.Manager):
    def get_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(PictureManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Picture(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    folder = models.CharField(max_length=20)
    file_name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PictureManager()

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def __unicode__(self):
        return str(self.file_name)

    def __str__(self):
        return str(self.file_name)