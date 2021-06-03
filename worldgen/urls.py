from django.urls import include, path
from rest_framework import routers
from .views import roll_table_views

router = routers.DefaultRouter()
router.register(r'RollTables', roll_table_views.GetAllRollTablesView)

urlpatterns = [
    path('', include(router.urls)),
    path('/api/', include('rest_framework.urls', namespace='rest_framework'))
]
