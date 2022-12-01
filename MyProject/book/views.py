from django.shortcuts import render, redirect
from .models import Voo, VooReal
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .forms import VooFormulario, VooFormularioUpdate, RelatorioFormulario, VooRealFormularioUpdate
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

# Create your views here.
@login_required(login_url='/accounts/login')
def crud(request):
    voo = list(Voo.objects.values())
    template = loader.get_template("CRUDPage.html")
    context = {'voo': voo}
    return HttpResponse(template.render(context, request))

# Definir: o que é o relatório
# O que vc precisa pro relatório: datas, quais voos
# O Forms de inputs de coisas pro relatório
# fzr pdf
@login_required(login_url='/accounts/login')
@permission_required('book.access_relatorio', raise_exception= PermissionDenied)
def relatorio(request):

    return render(request, "relatorio.html")

@login_required(login_url='/accounts/login')
@permission_required('book.add_voo')
def vooForm(request):
    form = VooFormulario()
    if request.method == 'POST':
        form = VooFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud')
    context = {'form': form}
    return render(request, 'vooForm.html', context)

@login_required(login_url='/accounts/login')
@permission_required('book.generate_relatorio')
def relatorioForm(request):
    form = RelatorioFormulario()
    if request.method == 'POST':
        form = RelatorioFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/relatorio')
    context = {'form': form}
    return render(request, 'relatorioForm.html', context)

@login_required(login_url='/accounts/login')
@permission_required('book.change_voo_real')
def vooUpdateForm(request, pk):
    vooReal1 = VooReal.objects.get(ID=pk)
    initial_data={'DH_REAL_CHEGADA':vooReal1.DH_REAL_CHEGADA,'DH_REAL_SAIDA':vooReal1.DH_REAL_SAIDA,'NM_STATUS':vooReal1.NM_STATUS}
    form2 = VooRealFormularioUpdate(initial=initial_data)
    if request.method == 'POST':
        form2 = VooRealFormularioUpdate(request.POST, instance=vooReal1)
        if form2.is_valid():
            form2.save()
            return redirect('/atualizarvoo')
    context = {'form': form2}
    return render(request, 'vooForm.html', context)


#def login(request):
 #  return render(request, "Login.html")


def My_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/crud')
    else:
        return redirect('accounts/login/')
    return render(request, 'registration/Login.html')

@login_required(login_url='/accounts/login')
@permission_required('book.access_atualizar', raise_exception= PermissionDenied)
def updateflight(request):
    voo = Voo.objects.values()
    vooReal = list(VooReal.objects.values())
    vooReal = list(voo.values())
    vooReal =  list(VooReal.objects.select_related("ID_VOO").all())
    template = loader.get_template("updateflight.html")
    context = {'vooReal': vooReal,'voo': voo}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/accounts/login')
@permission_required('book.delete_voo')
def deleteVoo(request, pk):
    voo = Voo.objects.get(ID=pk)
    if request.method == "POST":
        voo.delete()
        return redirect('/crud')
    context = { 'item': voo }
    return render(request, 'deleteVoo.html', context)
