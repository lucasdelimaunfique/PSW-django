from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def cadastro(request):
    #return HttpResponse('Ola mundo')
    #print(request.method)
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        ## verificar senha se são iguais
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, ' As senha não são iguais')
            # vai retornar um alert que vai ser um ERROR que está configurado no settings com a msg entre ' '
            return redirect('/usuarios/cadastro')
        
        ## verificar senha tem 6 digitos
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, ' Senha de pelo menos 6 digitos')
            return redirect('/usuarios/cadastro')
        
        # Verificar se o user não está cadastrado 
        users = User.objects.filter(username=username) ## vai verificar na tabela auth_user, e fazer um filtro só na coluna username se já possui o username que está tentando adicionar
        print (users.exists())      #vai retorna False se não existe e TRUE se existir 

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Ja existe esse usuario')
            return redirect('/usuarios/cadastro')

        #Para cadastrar usuarios no banco 
        user = User.objects.create_user(
            username = username,
            password = senha
        )
        
        return redirect('/usuarios/logar')
        #return HttpResponse(f'{username},{senha},{confirmar_senha}')