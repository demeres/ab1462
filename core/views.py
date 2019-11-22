from django.shortcuts import render,redirect
from core.models import Cliente
from core.form import FormClient

# Create your views here.


def home(request):
    return render(request, 'core/index.html' )

def cadastro (request):
    form = FormClient(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect ('url_principal')
    return render(request,'core/cadastro.html', {'form':form})

def listagem (request):
    dados = Cliente.objects.all()
    return render(request,'core/listagem.html',{'dados': dados})
