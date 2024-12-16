from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm
from .serializers import InscritoSerializer, InstitucionSerializer

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

class InscritoAPIView(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def institucion_api_view(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def institucion_detail_api_view(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    serializer = InstitucionSerializer(institucion)
    return Response(serializer.data)

@api_view(['GET'])
def autor_api_view(request):
    return Response({
        "Nombre": "Emanuel Gutierrez",
        "Email": "emanuel.gutierrez07@inacapmail.cl",
        "Proyecto": "Gutierrez_Emanuel_FINAL"
    })
