
from .views import ClientesAPIView
from django.urls import path


app_name = 'clientes'

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'', get)

urlpatterns = [
    path('', ClientesAPIView.as_view(), name='get-clientes'),
    path('<int:pk>/', ClientesAPIView.as_view(), name='detail-clientes')
]
