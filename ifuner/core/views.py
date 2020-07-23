from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def login(request):
    template_name = 'index.html'
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("email: {}  senha: {} ".format(username, password))

        usuario = authenticate(request, username=username, password=password)
        print("usuario ", usuario)
        if usuario is not None:
            # login(request, usuario)
            print("usuario ", usuario)
            form_login = "index"
            return redirect('index')
        else:
           form_login = "login"

    else:
        form_login = "login"

    return render(request, 'login.html', {'form_login': form_login})


