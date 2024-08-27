from django.urls import path
from appfinalds import views
from appfinalds.views import *

urlpatterns = [
    path('', inicio, name = 'inicio'),    
    path('asesores/', asesores, name = "asesores"),
    path('evaluadores/', evaluadores, name = "evaluadores"),
    path('evaluaciones/', evaluaciones, name = "evaluaciones"),
    path('about/', about, name = "about"),
]
formularios = [
    path('agregar_asesores/', views.agregar_asesores, name = 'agregar_asesores'),  
    path('agregar_evaluadores/', views.agregar_evaluadores, name = 'agregar_evaluadores'),  
    path('agregar_evaluaciones/', views.agregar_evaluaciones, name = 'agregar_evaluaciones'),  
]
urlpatterns += formularios


busqueda = [
    path('busqueda_asesor', views.busqueda_asesor, name = 'busqueda_asesor'),
    path('find_asesores/', views.find_asesores, name = 'find_asesores'), 
    path('busqueda_evaluador', views.busqueda_evaluador, name = 'busqueda_evaluador'),
    path('find_evaluador/', views.find_evaluador, name = 'find_evaluador'), 
    path('busqueda_evaluacion', views.busqueda_evaluacion, name = 'busqueda_evaluacion'),
    path('find_evaluacion/', views.find_evaluacion, name = 'find_evaluacion'), 
]

urlpatterns += busqueda

