from django import template

register = template.Library()

@register.filter
def active_page(name, page):
    class_active = ''
    if name == page:
        class_active = 'class = active'
    return class_active