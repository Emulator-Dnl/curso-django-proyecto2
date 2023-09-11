from django.urls import path
# Del directorio actual imoprtamos las vistas
from . import views

from django.conf import settings

urlpatterns = [
    path('', views.services, name="services"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
