from django.urls import path
from accounts.views import Register
urlpatterns = [
    path('accounts/', Register, name="Registrarse" ),
]