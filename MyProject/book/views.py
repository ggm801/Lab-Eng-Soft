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
from django.utils import timezone


#CRUD Page

@login_required(login_url='/accounts/login')
def crud(request):
    voo = list(Voo.objects.values())
    template = loader.get_template("CRUDPage.html")
    context = {'voo': voo}
    return HttpResponse(template.render(context, request))


# Relatorio Page

@login_required(login_url='/accounts/login')
@permission_required('book.access_relatorio', raise_exception= PermissionDenied)
def relatorio(request) :
    if request.method == "POST" :
      #  print('1')
        form = RelatorioFormulario(request.POST)
        if form.is_valid():
        #    print('2')
            relatorio = form.cleaned_data['relatorio']
            DH_PREVISTO_CHEGADA_i = form.cleaned_data['DH_PREVISTO_CHEGADA_i']
            DH_PREVISTO_CHEGADA_f = form.cleaned_data['DH_PREVISTO_CHEGADA_f']
          #  print(relatorio)
         #   print(DH_PREVISTO_CHEGADA_i)
         #   print(DH_PREVISTO_CHEGADA_f)
            return render(request, "relatorio.html")
    else:
        return render(request, "relatorio.html")


#Addicionar Voo Form

@login_required(login_url='/accounts/login')
@permission_required('book.add_voo')
def vooForm(request):
    form = VooFormulario()
    if request.method == 'POST':
        form = VooFormulario(request.POST)
        if form.is_valid():
            form.save()
            id = form.cleaned_data.get("ID_VOO")
            data_cheg = form.data.get("DH_PREVISTO_CHEGADA")
            data_saida = form.data.get("DH_PREVISTO_SAIDA")
            voo1 = Voo.objects.get(ID_VOO=id)
            VooReal.objects.create(ID_VOO=voo1, DH_REAL_SAIDA=data_saida, DH_REAL_CHEGADA=data_cheg )
            return redirect('/crud')
    context = {'form': form}
    return render(request, 'vooForm.html', context)


#Relatorio Form

@login_required(login_url='/accounts/login')
@permission_required('book.generate_relatorio')
def relatorioForm(request):
    form = RelatorioFormulario()
    if request.method == 'POST':
        form = RelatorioFormulario(request.POST)
        data_inicio = form.data.get('data_inicio')
        data_fim = form.data.get('data_fim')
        voos = VooReal.objects.filter(DH_REAL_SAIDA__range=[data_inicio, data_fim])
        contagem = voos.count()
        context = {
                'voos':voos, 
                'contagem':contagem, 
                'data_inicio': data_inicio, 
                'data_fim' : data_fim,
            }
        return render(request, 'relatorio.html', context)
    context={'form' : form}
    return render(request, 'relatorioForm.html', context)




#Atualizar dados do voo Real : AtualizarVoo
#Atualiza o status se é possivel e atualiza os horarios quando o status "Em Voo" e "Atterissado" são atualizados

@login_required(login_url='/accounts/login')
@permission_required('book.change_voo_real')
def vooUpdateForm(request, pk):
    vooReal1 = VooReal.objects.get(ID=pk)
    status_atual = vooReal1.NM_STATUS
    form2 = VooRealFormularioUpdate()
    if request.method == 'POST':
        form2 = VooRealFormularioUpdate(request.POST, instance=vooReal1)
        if status_atual=="EM" :
            if form2.data.get('NM_STATUS')=="Cancelado" or form2.data.get('NM_STATUS')=="Programado" :
                form2.save()
        else : 
            if check_status_order_partida(status_atual, form2.data.get('NM_STATUS') ) :
                if form2.data.get('NM_STATUS') == 'Em voo' :
                    vooReal1.DH_REAL_SAIDA=timezone.localtime(timezone.now())
                    form2.save()
                elif form2.data.get('NM_STATUS') == 'Atterissado' :
                    vooReal1.DH_REAL_CHEGADA=timezone.localtime(timezone.now())
                    form2.save()
                else : form2.save()
            return redirect('/atualizarvoo')
    context = {'form': form2}
    return render(request, 'vooForm.html', context)


#Fonção para verificar que a atualização do voo é possivel

def check_status_order_partida(status_now, status_applied):
    status_order = {'Programado': 1,
        'Embarcando': 2,
        'Cancelado': 9,
        'Taxeando': 3,
        'Pronto': 4,
        'Autorizado': 5,
        'Em voo': 6,
        'Pousando': 7,
        'Atterissado': 8, 
    }
    
    if status_order[status_now] + 1 ==  status_order[status_applied]:
        return status_applied
    else:
        return False



#Update Voo CRUD Page

@login_required(login_url='/accounts/login')
@permission_required('book.change_voo')
def vooUpdateForm2(request, pk):
    voo1 = Voo.objects.get(ID=pk)
    initial_data={'ID' : voo1.ID, 'DH_PREVISTO_SAIDA' : voo1.DH_PREVISTO_SAIDA,'DH_PREVISTO_CHEGADA' : voo1.DH_PREVISTO_CHEGADA, 'NM_AEROPORTO_SAIDA' : voo1.NM_AEROPORTO_SAIDA, 'NM_AEROPORTO_CHEGADA' : voo1.NM_AEROPORTO_CHEGADA,'NM_COMPANHIA_AEREA': voo1.NM_COMPANHIA_AEREA, 'ID_VOO':voo1.ID_VOO}
    form = VooFormularioUpdate(initial=initial_data)
    if request.method == 'POST':
        form = VooFormularioUpdate(request.POST, instance=voo1)
        if form.is_valid():
            form.save()
            return redirect('/crud')
    context = {'form': form}
    return render(request, 'vooForm.html', context)


#Login Page

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


#AtualizarVoo Page

@login_required(login_url='/accounts/login')
@permission_required('book.access_atualizar', raise_exception= PermissionDenied)
def updateflight(request):
    voo = Voo.objects.values()
    vooReal =  list(VooReal.objects.select_related("ID_VOO").all())
    template = loader.get_template("updateflight.html")
    context = {'vooReal': vooReal,'voo': voo}
    return HttpResponse(template.render(context, request))


#DeleteVoo

@login_required(login_url='/accounts/login')
@permission_required('book.delete_voo')
def deleteVoo(request, pk):
    voo = Voo.objects.get(ID=pk)
    if request.method == "POST":
        voo.delete()
        return redirect('/crud')
    context = { 'item': voo }
    return render(request, 'deleteVoo.html', context)

