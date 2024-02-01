from django.urls import path

from apps.menu.views import menu_view


urlpatterns = [
    path('menu/', menu_view, name="menu_view"),
]
