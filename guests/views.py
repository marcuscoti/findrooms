# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from forms import GuestForm
from django.utils import timezone
from models import Guest
from accounts.models import Account
from locations.models import State, City


# Create your views here.
class GuestCreateView(LoginRequiredMixin, CreateView):
    """View create Guest profile
    """
    model = Guest
    form_class = GuestForm
    template_name = "guests/guest_create.html"
    success_url = reverse_lazy('guests:list')

    def form_valid(self, form):
        account = Account.objects.get(user=self.request.user)
        form.instance.account = account
        return super(GuestCreateView, self).form_valid(form)


class GuestEditView(LoginRequiredMixin, UpdateView):
    """View edit Guest profile
    """
    model = Guest
    form_class = GuestForm
    template_name = "guests/guest_edit.html"
    success_url = reverse_lazy('guests:list')

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return Guest.objects.filter(account=account)


class GuestDetailView(DetailView):
    """View detail Guest Profile - NOT USED
    """
    model = Guest
    template_name = "guests/guest_detail.html"
    context_object_name = 'guest'

    def get_context_data(self, **kwargs):
        context = super(GuestDetailView, self).get_context_data(**kwargs)
        return context


class GuestListView(LoginRequiredMixin, ListView):
    """View list Guests by specific account
    """
    context_object_name = 'guest_list'
    template_name = "guests/guest_list.html"

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        queryset_list = Guest.objects.filter(account=account)
        return queryset_list

    def get_context_data(self, **kwargs):
        context = super(GuestListView, self).get_context_data(**kwargs)
        account = Account.objects.get(user=self.request.user)
        context['count_guests'] = Guest.objects.filter(account=account).count()
        return context



class GuestDeleteView(LoginRequiredMixin, DeleteView):
    """View delete Guest profile
    """
    model = Guest
    success_url = reverse_lazy('guests:list')

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return Guest.objects.filter(account=account)


@login_required
def guest_active_toggle(request, pk):
    """View to active/deactive Guest profile
    """
    account = Account.objects.get(user=request.user)
    guest = Guest.objects.get(pk=pk, account=account)
    guest.active_toogle()
    guest.save()
    return redirect('guests:list')