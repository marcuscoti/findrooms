# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import RoomCreateView, RoomEditView, RoomListView, RoomDetailView

urlpatterns = [
    url(r'^create/$', RoomCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)$', RoomDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', RoomEditView.as_view(), name='update'),
    url(r'^list/$', RoomListView.as_view(), name='list'),
]