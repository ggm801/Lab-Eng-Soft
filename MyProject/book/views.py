from django.shortcuts import render

# Create your views here.


def crud(request):
    return render(request, "CRUDPage.html")

def login(request):
    return render(request, "LogIn.html")

def relatorio(request):
    return render(request, "relatorio.html")