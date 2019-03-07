# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import ajax_load_cities

urlpatterns = [
    url(r'^ajax/load-cities/$', ajax_load_cities, name='ajax_load_cities'),
]