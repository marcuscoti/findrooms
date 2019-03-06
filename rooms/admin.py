# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Room
from django.contrib import admin

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room

    list_display = ('title', 'type')
    list_display_links = ('title', 'type')
    # list_filter = ('leader', 'state',)
    # search_filters = ('name', 'description',)


admin.site.register(Room, RoomAdmin)