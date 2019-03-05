# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Account
from django.contrib import admin


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    class Meta:
        model = Account

    list_display = ('user', 'whatsapp')
    list_display_links = ('user',)
    # list_filter = ('leader', 'state',)
    # search_filters = ('name', 'description',)


admin.site.register(Account, AccountAdmin)