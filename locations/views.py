# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import State, City

# Create your views here.
def ajax_load_cities(request):
   state = request.GET.get('state', None)
   cities = City.objects.filter(state=state)
   return render(request, '_ajax_cities_droplist.html', {'cities': cities})