from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm

# Vistas basadas en clases (CBV) para Inscritos
class InscritoListView(ListView):
    model = Inscrito
    template_name = "inscritos/inscrito_list.html"
    context_object_name = "inscritos"

class InscritoDetailView(DetailView):
    model = Inscrito
    template_name = "inscritos/inscrito_detail.html"

class InscritoCreateView(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = "inscritos/inscrito_form.html"
    success_url = reverse_lazy('inscrito-list')

class InscritoUpdateView(UpdateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = "inscritos/inscrito_form.html"
    success_url = reverse_lazy('inscrito-list')

class InscritoDeleteView(DeleteView):
    model = Inscrito
    template_name = "inscritos/inscrito_confirm_delete.html"
    success_url = reverse_lazy('inscrito-list')

# Vistas basadas en clases (CBV) para Instituciones
class InstitucionListView(ListView):
    model = Institucion
    template_name = "instituciones/institucion_list.html"
    context_object_name = "instituciones"

class InstitucionDetailView(DetailView):
    model = Institucion
    template_name = "instituciones/institucion_detail.html"

class InstitucionCreateView(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = "instituciones/institucion_form.html"
    success_url = reverse_lazy('institucion-list')

class InstitucionUpdateView(UpdateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = "instituciones/institucion_form.html"
    success_url = reverse_lazy('institucion-list')

class InstitucionDeleteView(DeleteView):
    model = Institucion
    template_name = "instituciones/institucion_confirm_delete.html"
    success_url = reverse_lazy('institucion-list')