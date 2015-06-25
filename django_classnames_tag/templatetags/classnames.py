from django.template import Library

register = Library()


@register.simple_tag
def classnames(**kwargs):
    return ' '.join(key for key, value in kwargs.items() if value)


@register.filter
def gte(value, arg):
    return value >= arg


@register.filter
def gt(value, arg):
    return value > arg


@register.filter
def lte(value, arg):
    return value <= arg


@register.filter
def lt(value, arg):
    return value < arg


@register.filter
def eq(value, arg):
    return value == arg
