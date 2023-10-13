from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('transações/', views.transacoes, name='transacoes'),
    path('nova_transação', views.nova_transacao, name='nova_transacao'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('desenvolvedor/', views.desenvolvedor, name="desenvolvedor"),
    path('suporte/', views.suporte, name='suporte'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.sair, name='sair') 
]
