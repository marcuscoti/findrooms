# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import RoomCreateView, RoomEditView, RoomListView, RoomDetailView, room_active_toggle, RoomDeleteView

urlpatterns = [
    url(r'^create/$', RoomCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)$', RoomDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', RoomEditView.as_view(), name='edit'),
    url(r'^active/(?P<pk>[0-9]+)$', room_active_toggle, name='active'),
    url(r'^delete/(?P<pk>[0-9]+)$', RoomDeleteView.as_view(), name='delete'),
    url(r'^list/$', RoomListView.as_view(), name='list'),
]