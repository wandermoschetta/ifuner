from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def login(request):
    template_name = 'index.html'
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("email: {}  senha: {} ".format(username, password))
        user = auth.authenticate(username=username, password=password)
        print("usuario ", user)
        if user is not None:
            auth.login(request, user)
            print("usuario ", user)
            return redirect('/')
        else:
            messages.info(request, 'Usuário ou senha inválido.')
            return redirect('/login')
    else:
        return render(request, 'login.html')
