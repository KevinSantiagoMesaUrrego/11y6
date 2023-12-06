from django.urls import path
from compra.views import compra_crear,compra_listar,compra_modificar,compra_eliminar,eliminar_detalle_compra
from compra.views import compra_finalizar
from compra.views import detalle_compra_listar, detalle_compra_crear, detalle_compra_modificar, detalle_compra_eliminar
from compra.views import evento_listar, evento_crear, evento_modificar, evento_eliminar , ver_detalle
from compra.views import proveedor_listar, proveedor_crear, proveedor_modificar, proveedor_eliminar

urlpatterns = [
    path('compra/', compra_listar, name="compra"),
    path('compra/crear/', compra_crear, name="compra-crear"),
    path('compra/modificar/<int:pk>/', compra_modificar, name="compra-modificar"),
    path('compra/eliminar/<int:pk>/', compra_eliminar, name="compra-eliminar"),
    path('detalle_compra/<int:pk>', detalle_compra_listar, name="detalle_compra"),
    path('detalle_compra/crear/', detalle_compra_crear, name="detalle_compra-crear"),
    path('detalle_compra/modificar/<int:pk>/', detalle_compra_modificar, name="detalle_compra-modificar"),
    path('detalle_compra/eliminar/<int:pk>/', detalle_compra_eliminar, name="detalle_compra-eliminar"),
    path('evento/', evento_listar, name="evento"),
    path('evento/crear/', evento_crear, name="evento-crear"),
    path('evento/modificar/<int:pk>/', evento_modificar, name="evento-modificar"),
    path('evento/eliminar/<int:pk>/', evento_eliminar, name="evento-eliminar"),
    path('proveedor/', proveedor_listar, name="proveedor"),
    path('proveedor/crear/', proveedor_crear, name="proveedor-crear"),
    path('proveedor/modificar/<int:pk>/', proveedor_modificar, name="proveedor-modificar"),
    path('proveedor/eliminar/<int:pk>/', proveedor_eliminar, name="proveedor-eliminar"),
    path('ver_detalle/<int:pk>/', ver_detalle ,name='ver_detalle'),
    path('compra/detalle_compra/', detalle_compra_listar ,name='detalle-compras'),
    path('compra_finalizar/<int:pk>/', compra_finalizar ,name='compra_finalizar'),
    path('eliminar_detalle_compra/<int:pk>/', eliminar_detalle_compra ,name='eliminar_detalle_compra'),
]