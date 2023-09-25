from django import template
from ..models import language_choice
register = template.Library()

@register.filter
def convert_language_value(value):
    return dict(language_choice)[value]