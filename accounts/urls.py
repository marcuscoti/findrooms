# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import AccountRegister, LoginView, AccountUpdate, \
    AccountEmailChange, \
    AccountPasswordChange, \
    logout_view, \
    confirm_recover_password, \
    Recover, \
    AccountDashboard,\
    AccountAnnouncements

urlpatterns = [
    url(r'^register/$', AccountRegister.as_view(), name='register'),
    url(r'^dashboard/$', AccountDashboard.as_view(), name='dashboard'),
    url(r'^announcements/$', AccountAnnouncements.as_view(), name='list_announcements'),
    url(r'^edit/(?P<pk>[0-9]+)$', AccountUpdate.as_view(), name='update'),
    url(r'^change-email/(?P<pk>[0-9]+)$', AccountEmailChange.as_view(), name='change_email'),
    url(r'^change-password/(?P<pk>[0-9]+)$', AccountPasswordChange.as_view(), name='change_password'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^recover/$', Recover.as_view(), name='recover_password'),
    url(r'^confirmrecover/(?P<token>[\w-]+)/$', confirm_recover_password, name='confirm_recover'),
]
