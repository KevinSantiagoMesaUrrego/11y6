from django.urls import path
from inventario.views import producto_crear,producto_listar,producto_modificar,producto_eliminar
from inventario.views import marca_crear,marca_listar,marca_modificar,marca_eliminar
from inventario.views import presentacion_crear,presentacion_listar,presentacion_modificar,presentacion_eliminar
from inventario.views import unidadmedida_crear,unidadmedida_listar,unidadmedida_modificar,unidadmedida_eliminar
from inventario.views import consumotrabajador_crear,consumotrabajador_listar,consumotrabajador_modificar,consumotrabajador_eliminar

urlpatterns = [
    path('producto/', producto_listar, name="producto" ),
    path('producto/crear/', producto_crear, name="producto-crear"),
    path('producto/modificar/<int:pk>/', producto_modificar, name="producto-modificar"),
    path('producto/eliminar/<int:pk>/', producto_eliminar, name="producto-eliminar"),
    path('marca/', marca_listar, name="marca"),
    path('marca/crear/', marca_crear, name="marca-crear"),
    path('marca/modificar/<int:pk>/', marca_modificar, name="marca-modificar"),
    path('marca/eliminar/<int:pk>/', marca_eliminar, name="marca-eliminar"),
    path('presentacion/',presentacion_listar,name="presentacion"),
    path('presentacion/crear/',presentacion_crear,name="presentacion-crear"),
    path('presentacion/modifcar/<int:pk>/',presentacion_modificar,name="presentacion-modificar"),
    path('presentacion/eliminar/<int:pk>/',presentacion_eliminar,name="presentacion-eliminar"),
    path('unidadmedida/',unidadmedida_listar,name="unidadmedida"),
    path('unidadmedida/crear/',unidadmedida_crear,name="unidadmedida-crear"),
    path('unidadmedida/modificar/<int:pk>/',unidadmedida_modificar,name="unidadmedida-modificar"),
    path('unidadmedida/eliminar/<int:pk>/',unidadmedida_eliminar,name="unidadmedida-eliminar"),
    path('consumotrabajador/',consumotrabajador_listar,name="consumotrabajador"),
    path('consumotrabajador/crear/',consumotrabajador_crear,name="consumotrabajador-crear"),
    path('consumotrabajador/modificar/<int:pk>/',consumotrabajador_modificar,name="consumotrabajador-modificar"),
    path('consumotrabajador/eliminar/<int:pk>/',consumotrabajador_eliminar,name="consumotrabajador-eliminar"),
]