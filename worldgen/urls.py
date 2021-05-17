from django.urls import path

from .views import views, treasure_views

urlpatterns = [
    path('', views.index, name='index'),
    path('treasure', treasure_views.treasure, name='treasure')
]