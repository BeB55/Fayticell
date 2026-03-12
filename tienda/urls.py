from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('todos/', views.todos_productos, name='todos_productos'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path("producto/<int:producto_id>/editar/", views.editar_producto, name="editar_producto"),
    path("producto/<int:producto_id>/eliminar/", views.eliminar_producto, name="eliminar_producto"),


]
