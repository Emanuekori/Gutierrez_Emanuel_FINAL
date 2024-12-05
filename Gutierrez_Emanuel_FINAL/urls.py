from django.urls import path
from Gut_Ema_FINAL_APP .views import (InscritoListView, InscritoDetailView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView, institucion_list, institucion_create) 

urlpatterns = [
    path('', InscritoListView.as_view(), name='index'),
    path('inscritos/', InscritoListView.as_view(), name='inscrito-list'),
    path('inscritos/<int:pk>/', InscritoDetailView.as_view(), name='inscrito-detail'),
    path('inscritos/create/', InscritoCreateView.as_view(), name='inscrito-create'),
    path('inscritos/<int:pk>/update/', InscritoUpdateView.as_view(), name='inscrito-update'),
    path('inscritos/<int:pk>/delete/', InscritoDeleteView.as_view(), name='inscrito-delete'),
    path('instituciones/', institucion_list, name='institucion-list'),
    path('instituciones/create/', institucion_create, name='institucion-create'),
]
