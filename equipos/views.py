from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from equipos.forms import EquiposForm
from equipos.models import Equipo
from django.db.models import QuerySet
from django.urls import reverse_lazy


# Create your views here.
class EquiposListView(ListView):
    model = Equipo
    template_name = 'equipos/equipos.html'


    def get_queryset(self) -> QuerySet[Equipo]:
        return self.model.objects.only('id', 'imei')


class EquiposCreateUpdateViewMixin:
    model = Equipo
    form_class = EquiposForm
    # fields = ['imei', 'simcard', 'operador', 'activo', 'cliente']
    template_name = 'equipos/equipo-crear.html'
    success_url = reverse_lazy('equipos:get')


class EquiposCreateView(EquiposCreateUpdateViewMixin, CreateView):
    pass


class EquiposUpdateView(EquiposCreateUpdateViewMixin, UpdateView):
    def get_queryset(self) -> QuerySet[Equipo]:
        return self.model.objects.all()


class EquiposDetailView(DetailView):
    model = Equipo
    fields = ['imei', 'simcard', 'operador', 'activo', 'cliente']
    template_name = 'equipos/equipo-detalle.html'
    context_object_name = 'instancia'


class EquipoDeleteview(DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipos:get')