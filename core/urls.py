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

]
