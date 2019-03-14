# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Guest
from django.contrib import admin

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    class Meta:
        model = Guest

    list_display = ('name', 'gender', 'age')
    list_display_links = ('name', 'gender', 'age')
    # list_filter = ('leader', 'state',)
    # search_filters = ('name', 'description',)


admin.site.register(Guest, GuestAdmin)