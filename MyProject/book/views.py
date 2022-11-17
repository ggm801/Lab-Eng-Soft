from django.shortcuts import render, redirect
from .models import Voo, VooReal
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .forms import VooFormulario, VooFormularioUpdate
from django.contrib.auth import authenticate,login
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
    form1 = VooFormularioUpdate(instance=voo)
    if request.method == 'POST':
        form2 = VooFormularioUpdate(request.POST, instance=voo)
        if form2.is_valid():
            form2.save()
            return redirect('/crud')
    context = {'form': form1}
    return render(request, 'vooForm.html', context)


#def login(request):
 #  return render(request, "Login.html")


def My_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('relatorio')
    else:
        return redirect('accounts/login/')
    return render(request, 'registration/Login.html')


def updateflight(request):
    vooReal = list(VooReal.objects.values())
    template = loader.get_template("updateflight.html")
    context = {'voo': vooReal}
    return HttpResponse(template.render(context, request))

def deleteVoo(request, pk):
    voo = Voo.objects.get(ID=pk)
    if request.method == "POST":
        voo.delete()
        return redirect('/crud')
    context = { 'item': voo }
    return render(request, 'deleteVoo.html', context)
