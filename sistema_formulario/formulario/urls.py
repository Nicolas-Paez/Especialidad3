from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_formulario, name='crear_formulario'),
    path('formulario/<int:formulario_id>/responder/', views.responder_formulario, name='responder_formulario'),
    path('formulario/<int:formulario_id>/', views.ver_formulario, name='ver_formulario'),  
    path('formulario/eliminar/<int:id>/', views.eliminar_formulario, name='eliminar_formulario'),
]
