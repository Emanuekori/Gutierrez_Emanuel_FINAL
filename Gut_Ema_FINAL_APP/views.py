from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm

# Vistas basadas en clases (CBV)
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

# Vistas basadas en funciones(FBV)
def institucion_list(request):
    instituciones = Institucion.objects.all()
    return render(request, 'instituciones/institucion_list.html', {'instituciones': instituciones})

def institucion_detail(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    return JsonResponse({'id': institucion.id, 'nombre': institucion.nombre})

def institucion_create(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Institución creada exitosamente'})
    else:
        form = InstitucionForm()
    return render(request, 'instituciones/institucion_form.html', {'form': form})
