from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='add_class_despesas')
def add_class_despesas(field, css_class):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={'class': css_class})
    return field


