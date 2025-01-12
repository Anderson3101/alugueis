from django import template

register = template.Library()

@register.filter(name="add_class_alugueis")
def add_class_alugueis(value, css_class):
    """Adiciona uma classe CSS ao widget do campo do formulário."""
    return value.as_widget(attrs={"class": css_class})
