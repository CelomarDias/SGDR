from django.shortcuts import render
from SGDR.models import SGDR
from SGDR.forms import SGDRForms

def index_agenda(request):
    if request.method == "POST":
        form = SGDRForms(request.POST)
        if form.is_valid():
            form.save()
    informacao = SGDR.objects.all()
    dados = {
        "informacao":informacao
    }
    return render(request, "index.html", context = dados)


def index_criacao(request):
    informacao = SGDRForms()
    dados = {
        "informacao": informacao 
        }
    return render(request, "index_criacao.html", context = dados)

def index_info(request,id_contato):
    informacao  = SGDR.objects.filter(id=id_contato).first()
    dados = {
        "informacao ":informacao 
    }
    return render(request, "index_info.html", context=dados)

def update_contato(request,id_contato):
    informacao  = SGDR.objects.filter(id=id_contato).first()
    if request.method == "POST":
        informacao .tipo = request.POST["tipo"]
        informacao .peso = request.POST["peso"]
        informacao .quantidade = request.POST["quantidade"]
        informacao .save()
        informacao  = SGDR.objects.all()
    dados = {
        "informacao ":informacao 
    }
    return render(request, "update_contato.html", context=dados)

def delete_contato(request,id_contato):
    SGDR.objects.filter(id=id_contato).delete()
    informacao  = SGDR.objects.all()
    dados = {
        "informacao ":informacao 
    }
    return render(request, "index.html", context=dados)


# Create your views here.
