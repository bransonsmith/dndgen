from django.urls import path

from .views import views, treasure_views, monster_views, world_views, roll_table_views

urlpatterns = [
    path('', views.index, name='index'),
    path('treasure', treasure_views.treasure, name='treasure'),
    path('monster', monster_views.monster, name='monster'),
    path('world', world_views.world, name='world'),
    path('roll_table/<str:roll_table_name>', roll_table_views.roll_table, name='roll_table'),
]