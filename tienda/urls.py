from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('todos/', views.todos_productos, name='todos_productos'),
]
