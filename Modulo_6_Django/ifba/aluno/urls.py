from django.contrib import admin
from django.urls import path, include
from .views import home,criar_aluno,editar,editar_aluno,cadastrar_aluno,update,deletar_aluno

urlpatterns = [
    path('', home),    
    path('aluno/', home),  
    path('criar_aluno/', criar_aluno, name="criar_aluno"),
    path('editar_aluno/', editar_aluno, name="editar_aluno"),
    path('cadastrar/', cadastrar_aluno, name="cadastrar"),
    path('editar/<int:id>',editar,name="editar"),
    path('update/<int:id>',update,name="update"),
    path('deletar_aluno/<int:id>',deletar_aluno,name="deletar_aluno")
]
