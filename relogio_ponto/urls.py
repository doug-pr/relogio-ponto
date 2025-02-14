from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_horario/', views.adicionar_horario, name='adicionar_horario'),
    path('excluir_horario/<int:id>', views.excluir_horario, name='excluir_horario'),
    path('atualizar_horario/<int:id>', views.atualizar_horario, name='atualizar_horario'),
]