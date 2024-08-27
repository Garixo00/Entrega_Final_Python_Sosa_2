from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views
from users.views import *

urlpatterns = [
    path('login/', views.login_request, name = "login"),
    path('register/', views.register, name = "register"),
    path('logout/', views.custom_logout, name='logout'),
    path('errorlogin/', views.errorlogin, name = "errorlogin"),
]

perfiles = [
    path('editar_perfil/', views.editar_perfil, name = "editar_perfil"),
    path('cambiar_pass/', views.CambiarPass.as_view(), name = "cambiar_pass"),
    path('perfil_ok/', views.perfil_ok, name = "perfil_ok"),
]

urlpatterns += perfiles

