from django.shortcuts import render
from .models import Voo
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .forms import VooFormulario

# Create your views here.


def crud(request):
    voo = list(Voo.objects.values())
    template = loader.get_template("CRUDPage.html")
    context = {'voo': voo}
    return HttpResponse(template.render(context, request))


def relatorio(request):
    return render(request, "relatorio.html")


def vooForm(request):
    form = VooFormulario()
    if request.method == 'POST':
        form = VooFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'vooForm.html', context)


def login(request):
    return render(request, "Login.html")


def updateflight(request):
    return render(request, "updateflight.html")

# def formpage(request):
#    return render(request, "formPage.html")
