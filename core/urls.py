from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('garantias/', views.garantias, name='garantias'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
