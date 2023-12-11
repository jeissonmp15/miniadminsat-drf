
from django.urls import path

from .viewsets import EquiposViewset
from rest_framework.routers import DefaultRouter

app_name = 'equipos'

router = DefaultRouter()
router.register(r'', EquiposViewset, basename='user')

app_name = 'equipos'

urlpatterns = router.urls
