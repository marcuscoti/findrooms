# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.views import View
from forms import RoomCreateForm, RoomEditForm
from django.utils import timezone
from models import Room


# Create your views here.
class RoomCreateView(CreateView):
    model = Room
    form_class = RoomCreateForm
    template_name = "room_create.html"

    def form_valid(self, form):
        #form.instance.created_by = self.request.user
        return super(RoomCreateView, self).form_valid(form)


class RoomEditView(UpdateView):
    model = Room
    form_class = RoomEditForm
    template_name = "room_edit.html"


class RoomDetailView(DetailView):
    model = Room
    template_name = "room_detail.html"
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        return context


class RoomListView(ListView):
    context_object_name = 'room_list'
    template_name = "room_list.html"

    def get_queryset(self):
        queryset_list = Room.objects.all()
        return queryset_list


def ajax_load_groups(request):
   project = request.GET.get('project', None)
   groups = Group.objects.filter(project_id=project)
   return render(request, 'group_dropdown_list_options.html', {'groups': groups})