from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/logar_usuario')
def crud(request):
    return render(request, "CRUDPage.html")


def login(request):
    return render(request, "LogIn.html")

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('relatorio')
        else:
            return render(request, 'login.html', {'form':AuthenticationForm(), 'error' : 'wrongpwd'})
    else :
        return render(request, 'login.html', {'form': AuthenticationForm()})

@login_required(login_url='/logar_usuario')
def relatorio(request):
    return render(request, "relatorio.html")

@login_required(login_url='/logar_usuario')
def updateflight(request):
    return render(request, "updateflight.html")
