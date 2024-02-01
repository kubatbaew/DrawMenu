from django import template

from apps.menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    menu = Menu.objects.filter(
        menu_name=menu_name,
        parent__isnull=True,
    )
    return {'menu': menu}
