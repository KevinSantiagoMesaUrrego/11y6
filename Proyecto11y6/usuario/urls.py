from django.urls import path
from usuario.views import persona_listar, persona_crear, persona_modificar, persona_eliminar
from usuario.views import eps_listar, eps_crear, eps_modificar, eps_eliminar
from usuario.views import turno_listar, turno_crear, turno_modificar, turno_eliminar
from usuario.views import trabajador_listar, trabajador_crear, trabajador_modificar, trabajador_eliminar

urlpatterns = [
    path('persona/', persona_listar, name="persona" ),
    path('persona/crear/', persona_crear, name="personas-crear" ),
    path('persona/modificar/<int:pk>/', persona_modificar, name="persona-modificar" ),
    path('persona/eliminar/<int:pk>/', persona_eliminar, name="persona-eliminar" ),
    path('eps/', eps_listar, name="eps" ),
    path('eps/crear/', eps_crear, name="eps-crear" ),
    path('eps/modificar/<int:pk>/', eps_modificar, name="eps-modificar" ),
    path('eps/eliminar/<int:pk>/', eps_eliminar, name="eps-eliminar" ),
    path('turno/', turno_listar, name="turno" ),
    path('turno/crear/', turno_crear, name="turno-crear" ),
    path('turno/modificar/<int:pk>/', turno_modificar, name="turno-modificar" ),
    path('turno/eliminar/<int:pk>/', turno_eliminar, name="turno-eliminar" ),
    path('trabajador/', trabajador_listar, name="trabajador" ),
    path('trabajador/crear/', trabajador_crear, name="trabajador-crear" ),
    path('trabajador/modificar/<int:pk>/', trabajador_modificar, name="trabajador-modificar" ),
    path('trabajador/eliminar/<int:pk>/', trabajador_eliminar, name="trabajador-eliminar" ),

]