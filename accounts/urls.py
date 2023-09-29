from django.urls import path

from accounts import views
from accounts.views import Register
urlpatterns = [
    path('account-register/',  views.register, name='Registrarse'),



]