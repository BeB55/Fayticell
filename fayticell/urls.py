from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),   # core maneja la página principal
    path('tienda/', include('tienda.urls')),  # tienda maneja lo específico
]
