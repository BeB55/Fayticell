from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Multiplica dos valores (precio × cantidad)."""
    try:
        return float(value) * int(arg)
    except (ValueError, TypeError):
        return 0
