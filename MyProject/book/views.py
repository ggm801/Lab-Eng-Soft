from django.shortcuts import render
from .models import Voo, VooReal, Usuario
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .forms import criarVoo
# Create your views here.


def crud(request):
    voo = list(Voo.objects.values())
    template = loader.get_template("CRUDPage.html")
    context = {'voo': voo}
    return HttpResponse(template.render(context, request))

def criarVoo(request):
     if request.method == "POST":
      vooForm = criarVoo(request.POST)


def relatorio(request):
    return render(request, "relatorio.html")


def updateflight(request):
    return render(request, "updateflight.html")

def formpage(request):
    return render(request, "formPage.html")
