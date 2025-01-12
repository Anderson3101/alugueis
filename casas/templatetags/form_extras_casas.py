from django import template

register = template.Library()

@register.filter(name='add_class_casas')
def add_class_casas(field, css_class):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={'class': css_class})
    return field


