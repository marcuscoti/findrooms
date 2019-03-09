# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import Room
from locations.models import State, City

class RoomCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomCreateForm, self).__init__(*args, **kwargs)
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
        model = Room
        exclude = ['active', 'account', 'updated', 'created']

        labels = {
            'title': 'Título do Anúncio',
            'building': 'Tipo de Estabelecimento',
            'type': 'Tipo de Quarto',
            'bathroom': 'Tipo de Banheiro',
            'gender': 'Gênero',
            'description': 'Descrição',
            'smoking': 'Aceita fumantes',
            'garage': 'Tem garagem',
            'include_bills': 'Contas inclusas',
            'visits': 'Aceita visitas',
            'internet': 'Internet no local',
            'furniture': 'Quarto mobiliado',
            'value': 'Mensalidade',
            'active': 'Ativo',
            'state': 'Estado',
            'city': 'Cidade',
            'region': 'Bairro',
            'cep': 'CEP',
            'contact_name': 'Nome do Contato',
        }


class RoomEditForm(forms.ModelForm):
    pass

