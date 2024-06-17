from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import EmpleadoForm
from .models import Empleado

class EmpleadoListView(generic.ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(SuccessMessageMixin, generic.CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado_list')
    success_message = "Empleado creado exitosamente"

class EmpleadoUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado_list')
    success_message = "Empleado actualizado exitosamente"

class EmpleadoDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')
    success_message = "Empleado eliminado exitosamente"
