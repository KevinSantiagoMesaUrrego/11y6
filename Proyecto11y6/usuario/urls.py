from django.urls import path

from usuario.views import persona_listar, persona_crear, persona_modificar, persona_eliminar

urlpatterns = [
    path('personas/', persona_listar, name="personas" ),
    path('personas/crear/', persona_crear, name="personas-crear" ),
    path('personas/modificar/<int:pk>/', persona_modificar, name="personas-modificar" ),
    path('personas/eliminar/<int:pk>/', persona_eliminar, name="personas-eliminar" ),

]