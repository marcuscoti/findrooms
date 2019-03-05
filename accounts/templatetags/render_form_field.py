from django import template

register = template.Library()

@register.inclusion_tag('_form_field.html')
def render_form_field(field):
    return {'field': field}

@register.inclusion_tag('_form_field_dis.html')
def render_field_disabled(field):
    return {'field': field}