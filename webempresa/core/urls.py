from django.urls import path
# Del directorio actual imoprtamos las vistas
from . import views

from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
