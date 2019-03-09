# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.inclusion_tag('tags/_form_field.html')
def render_form_field(field):
    return {'field': field}

@register.inclusion_tag('tags/_check_box.html')
def render_check_box(field):
    return {'field': field}

@register.inclusion_tag('tags/_form_card.html')
def render_form_card(title, field_type, fields):
    return {'fields': fields, 'title': title, 'field_type': field_type}

@register.inclusion_tag('tags/_form_field_dis.html')
def render_field_disabled(field):
    return {'field': field}

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter(name='boolfield')
def boolfield(value, arg):
    if value:
        if arg == 'accept':
            return "Aceita"
        if arg == 'yesno':
            return "Sim"
        if arg == 'has':
            return "Tem"
    else:
        if arg == 'accept':
            return "Não aceita"
        if arg == 'yesno':
            return "Não"
        if arg == 'has':
            return "Não tem"