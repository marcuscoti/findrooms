# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import Guest
from locations.models import State, City


class GuestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['city'].queryset = City.objects.none()
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state=state_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

    class Meta:
        model = Guest
        exclude = ['active', 'account', 'updated', 'created']

        labels = {
            'name': 'Nome',
            'gender': 'Gênero',
            'age': 'Idade',
            'description': 'Descrição',
            'work': 'Trabalha',
            'study': 'Estuda',
            'smoking': 'É fumante',
            'garage': 'Necessito de garagem para meu veículo',
            'max_value': 'Valor máximo (R$)',
            'state': 'Estado',
            'city': 'Cidade',
        }
