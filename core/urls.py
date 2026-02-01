from django.urls import path
from . import views
from .views import edit_profile, como_comprar

urlpatterns = [
    path('', views.home, name='home'),
    path('garantias/', views.garantias, name='garantias'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path("mi-cuenta/", views.mi_cuenta, name="mi_cuenta"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("como-comprar/", views.como_comprar, name="como_comprar"),
    path("carrito/", views.ver_carrito, name="carrito"),
    path("agregar-carrito/<int:producto_id>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path("eliminar-carrito/<int:producto_id>/", views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path("carrito/incrementar-cantidad/<int:producto_id>/", views.incrementar_cantidad, name="incrementar_cantidad"),
    path("carrito/disminuir-cantidad/<int:producto_id>/", views.disminuir_cantidad, name="disminuir_cantidad"),

]
