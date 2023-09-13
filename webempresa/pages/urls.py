from django.urls import path
# Del directorio actual imoprtamos las vistas
from . import views

# para poder emplear el id en la vista
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]