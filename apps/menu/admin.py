from django.contrib import admin

from apps.menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu_name']
    search_fields = ['title']
    list_filter = ['parent']
    