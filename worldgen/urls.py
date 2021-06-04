from django.urls import include, path
from rest_framework import routers
from .views import roll_table_views

router = routers.DefaultRouter()
router.register(r'RollTables', roll_table_views.RollTableViewSet)
router.register(r'RollTableEntrys', roll_table_views.LocationRollTableEntryViewSet)
router.register(r'LocationTypes', roll_table_views.LocationTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/api/', include('rest_framework.urls', namespace='rest_framework')),
    path('generate_roll_tables', roll_table_views.generate_roll_tables, name='generate_roll_tables'),
]
