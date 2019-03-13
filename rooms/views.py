# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from forms import RoomForm
from django.utils import timezone
from models import Room
from accounts.models import Account
from locations.models import State, City


# Create your views here.
class RoomCreateView(LoginRequiredMixin, CreateView):
    """View create Room
    """
    model = Room
    form_class = RoomForm
    template_name = "rooms/room_create.html"
    success_url = reverse_lazy('rooms:list')

    def form_valid(self, form):
        account = Account.objects.get(user=self.request.user)
        form.instance.account = account
        return super(RoomCreateView, self).form_valid(form)


class RoomEditView(LoginRequiredMixin, UpdateView):
    """View edit Room
    """
    model = Room
    form_class = RoomForm
    template_name = "rooms/room_edit.html"
    success_url = reverse_lazy('rooms:list')

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return Room.objects.filter(account=account)


class RoomDetailView(DetailView):
    """View detail Room - NOT USED
    """
    model = Room
    template_name = "rooms/room_detail.html"
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        return context


class RoomListView(LoginRequiredMixin, ListView):
    """View list Rooms by specific account
    """
    context_object_name = 'room_list'
    template_name = "rooms/room_list.html"

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        queryset_list = Room.objects.filter(account=account)
        return queryset_list


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    """View delete Rooms
    """
    model = Room
    success_url = reverse_lazy('rooms:list')

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return Room.objects.filter(account=account)


@login_required
def room_active_toggle(request, pk):
    """View to active/deactive Rooms
    """
    account = Account.objects.get(user=request.user)
    room = Room.objects.get(pk=pk, account=account)
    room.active_toogle()
    room.save()
    return redirect('rooms:list')