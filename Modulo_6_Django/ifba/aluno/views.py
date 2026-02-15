from django.shortcuts import render, redirect
from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {"alunos": alunos})


def cadastrar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    Aluno.objects.create(nome=nome, email=email)
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {"alunos": alunos})


def criar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    Aluno.objects.create(nome=nome, email=email)
    alunos = Aluno.objects.all()
    return render(request, 'criar_aluno.html', {"alunos": alunos})


def editar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    Aluno.objects.create(nome=nome, email=email)
    alunos = Aluno.objects.all()
    return render(request, 'criar_aluno.html', {"alunos": alunos})


def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, "update.html", {"aluno": aluno})


def update(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.email = email
    aluno.save()
    return redirect(home)


def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect(home)
