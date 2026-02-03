from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),   # core maneja la página principal
    path('tienda/', include('tienda.urls')),  # tienda maneja lo específico
    path('accounts/', include('allauth.urls')),  # allauth para autenticación
    path("test-email/", test_email, name="test_email"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)