
from django.urls import path

from .views import EquiposListView, EquiposCreateView, EquiposUpdateView, EquiposDetailView, EquipoDeleteview

app_name = 'equipos'

urlpatterns = [
    path('', EquiposListView.as_view(), name='get'),
    path('crear/', EquiposCreateView.as_view(), name='create'),
    path('<int:pk>/', EquiposUpdateView.as_view(), name='update'),
    path('<int:pk>/detalle/', EquiposDetailView.as_view(), name='detail'),
    path('<int:pk>/eliminar/', EquipoDeleteview.as_view(), name='delete'),
    
]
