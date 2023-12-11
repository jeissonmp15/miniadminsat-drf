
from django.urls import path

from .views import ActivosListAPIView, ActivosDetailAPIView

app_name = 'activos'

urlpatterns = [
    path('', ActivosListAPIView.as_view(), name='get-activos')
]
