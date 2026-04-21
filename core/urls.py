from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('formacao/', views.formacao, name='formacao'),
    path('cursos/', views.cursos, name='cursos'),
    path('projetos/', views.projetos, name='projetos'),
    path('contacto/', views.contacto, name='contacto'),
    path('cv/', views.cv, name='cv'),
    path('tests/', views.cv_view, name='tests'),
]