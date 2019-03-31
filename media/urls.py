# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import GuestCreateView, GuestListView, GuestDeleteView, GuestDetailView, guest_active_toggle, GuestEditView

urlpatterns = [
    url(r'^create/$', GuestCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)$', GuestDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', GuestEditView.as_view(), name='edit'),
    url(r'^active/(?P<pk>[0-9]+)$', guest_active_toggle, name='active'),
    url(r'^delete/(?P<pk>[0-9]+)$', GuestDeleteView.as_view(), name='delete'),
    url(r'^list/$', GuestListView.as_view(), name='list'),
]