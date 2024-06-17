from django.urls import path
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='empleado_list'),
    path('new/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('edit/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
]
