# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import Room


class RoomCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomCreateForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.none()
        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['group'].queryset = Group.objects.filter(project_id=project_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['group'].queryset = Group.objects.filter(project=self.instance.project)

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
            'smoking': 'Aceita fumantes?',
            'garage': 'Tem garagem?',
            'include_bills': 'Contas inclusas?',
            'visits': 'Aceita visitas?',
            'internet': 'Internet no local?',
            'furniture': 'Quarto mobiliado?',
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

