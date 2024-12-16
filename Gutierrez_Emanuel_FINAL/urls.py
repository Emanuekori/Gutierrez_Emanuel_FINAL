from django.urls import path
from django.views.generic.base import TemplateView
from Gut_Ema_FINAL_APP.views import (
    InscritoListView, InscritoDetailView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView,
    InstitucionListView, InstitucionDetailView, InstitucionCreateView, InstitucionUpdateView, InstitucionDeleteView,
    InscritoAPIView, institucion_api_view, institucion_detail_api_view, autor_api_view
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('inscritos/', InscritoListView.as_view(), name='inscrito-list'),
    path('inscritos/<int:pk>/', InscritoDetailView.as_view(), name='inscrito-detail'),
    path('inscritos/create/', InscritoCreateView.as_view(), name='inscrito-create'),
    path('inscritos/<int:pk>/update/', InscritoUpdateView.as_view(), name='inscrito-update'),
    path('inscritos/<int:pk>/delete/', InscritoDeleteView.as_view(), name='inscrito-delete'),
    path('instituciones/', InstitucionListView.as_view(), name='institucion-list'),
    path('instituciones/<int:pk>/', InstitucionDetailView.as_view(), name='institucion-detail'),
    path('instituciones/create/', InstitucionCreateView.as_view(), name='institucion-create'),
    path('instituciones/<int:pk>/update/', InstitucionUpdateView.as_view(), name='institucion-update'),
    path('instituciones/<int:pk>/delete/', InstitucionDeleteView.as_view(), name='institucion-delete'),
    path('api/inscritos/', InscritoAPIView.as_view(), name='inscrito-api'),
    path('api/instituciones/', institucion_api_view, name='institucion-api'),
    path('api/instituciones/<int:pk>/', institucion_detail_api_view, name='institucion-detail-api'),
    path('api/autor/', autor_api_view, name='autor-api'),
]
