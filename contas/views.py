from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from .form import *
import datetime
from .models import *
# Create your views here.

def index(request):
    data = {}
    return render(request, 'contas/index.html', data)

@login_required(login_url="/auth/login/")       
def home(request):
    data = {}
    data['ultimatransacao'] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)

@login_required(login_url="/auth/login/")
def transacoes(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/transacoes.html', data)

@login_required(login_url="/auth/login/")
def nova_transacao(request):
    data = {}
    data['tipos'] = Tipos.objects.all()
    data['categorias'] = Categoria.objects.all()
    data['now'] = datetime.datetime.now()
    
    if request.method == "GET":
        return render(request, 'contas/novatransacao.html', data)
    else:
        banco = request.POST.get('banco')
        valor = request.POST.get('valor')
        dia = request.POST.get('data')

        tipo = request.POST.get('tipo')
        registroTipo = Tipos.objects.get(nome=tipo)

        categoria = request.POST.get('categoria')
        registroCategoria = Categoria.objects.get(nome=categoria)

        descricao = request.POST.get('descricao')
        
        transacao = Transacao.objects.create(banco=banco, valor=valor, data=dia, tipo=registroTipo, categoria=registroCategoria, descricao=descricao)
        transacao.save()

        return redirect('transacoes')

@login_required(login_url="/auth/login/")
def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('transacoes')
    
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/novatransacao.html', data)

@login_required(login_url="/auth/login/")
def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('transacoes')

@login_required(login_url="/auth/login/")
def suporte(request):
    data = {}
    if request.method == "GET":
        return render(request, 'contas/suporte.html', data)
    else:
        return redirect('home')

@login_required(login_url="/auth/login/")
def desenvolvedor(request):
    data = {}
    return render(request, 'contas/desenvolvedor.html', data)

def cadastro(request):
    if request.method == "GET":
        return render(request, 'contas/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'contas/login.html')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('home')

def login(request):
    if request.method == "GET":
        return render(request, 'contas/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            return redirect('cadastro')
        
@login_required(login_url="/auth/login/")
def sair(request):
    logout(request)
    return redirect('index')