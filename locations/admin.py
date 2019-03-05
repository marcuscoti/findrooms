# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import State, City
from django.contrib import admin


# Register your models here.
class StateAdmin(admin.ModelAdmin):
    class Meta:
        model = State

    list_display = ('name', 'code')
    list_display_links = ('name', 'code')
    # list_filter = ('leader', 'state',)
    # search_filters = ('name', 'description',)


class CityAdmin(admin.ModelAdmin):
    class Meta:
        model = City

    list_display = ('name', 'state')
    list_display_links = ('name', 'state')
    # list_filter = ('leader', 'state',)
    # search_filters = ('name', 'description',)


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)