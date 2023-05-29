"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views

from base.views import principal, logout_user
# para las iamgenes
from django.conf import settings
from django.conf.urls.static import static
# para la gestion de login y contraseña
from django.contrib.auth import views as auth_views
from accounts.views import register

urlpatterns = [
    #gestion de login y contraseña
    path('',auth_views.LoginView.as_view(),name='inicio'),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('logout/',logout_user,name="logout"),
    path('admin/', admin.site.urls),
    path('inicio/', principal, name="index" ),
    path('inicio-guest/', principal, name="body-login" ),
    path('usuarios/', include('usuario.urls') ),
    path('ventas/', include('venta.urls')),
    path('compras/', include('compra.urls')),
    path('inventarios/',include('inventario.urls')),
    path('templates/partials/', include('accounts.urls')),
    path('account-register',  views.register, name='Registrarse')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
