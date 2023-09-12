from django.urls import path
# Del directorio actual imoprtamos las vistas
from . import views

from django.conf import settings

# para poder emplear el id en la vista
urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)