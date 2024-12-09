from django.urls import path
from Gut_Ema_FINAL_APP.views import (InscritoListView, InscritoDetailView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView,InstitucionListView, InstitucionDetailView, InstitucionCreateView, InstitucionUpdateView, InstitucionDeleteView)
from django.views.generic.base import TemplateView

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
]
