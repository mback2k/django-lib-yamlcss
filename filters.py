from django import template
from django.forms import widgets
from django.template.loader import render_to_string

register = template.Library()

@register.filter
def yamlform(form):
    return render_to_string('yamlform.html', { 'form': form })

@register.filter
def yamlform_field_type(field):
    try:
        widget = field.field.widget
    except AttributeError:
        widget = field.widget
    if isinstance(widget, widgets.Select):
        return 'select'
    elif isinstance(widget, widgets.CheckboxInput):
        return 'check'
    elif isinstance(widget, widgets.RadioInput):
        return 'check'
    return 'text'

@register.filter
def yamlform_field_id(field):
    try:
        widget = field.field.widget
    except AttributeError:
        widget = field.widget
    return widget.attrs.get(id, field.auto_id)
