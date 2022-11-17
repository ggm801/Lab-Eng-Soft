from django.shortcuts import render, redirect
from .models import Voo
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .forms import VooFormulario
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
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
            return redirect('/crud')
    context = {'form': form}
    return render(request, 'vooForm.html', context)


def vooUpdateForm(request, pk):
    voo = Voo.objects.get(ID=pk)
    form1 = VooFormulario(instance=voo)
    if request.method == 'POST':
        form2 = VooFormulario(request.POST, instance=voo)
        if form2.is_valid():
            form2.save()
            return redirect('/crud')
    context = {'form': form1}
    return render(request, 'vooForm.html', context)


#def login(request):
 #  return render(request, "Login.html")



def updateflight(request):
    return render(request, "updateflight.html")

def deleteVoo(request, pk):
    voo = Voo.objects.get(ID=pk)
    if request.method == "POST":
        voo.delete()
        return redirect('/crud')
    context = { 'item': voo }
    return render(request, 'deleteVoo.html', context)
