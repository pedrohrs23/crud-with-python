from django.shortcuts import render, redirect
from app.forms import ProcessosForm
from app.models import Processos
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        # REVER ESSA QUESTÃO POIS NÃO ACHA TODAS AS OPÇÕES 
        data['db'] = Processos.objects.filter(id__icontains=search)
        data['db'] = Processos.objects.filter(Protocolo__icontains=search)
        data['db'] = Processos.objects.filter(Status__icontains=search)
        data['db'] = Processos.objects.filter(Paciente__icontains=search)
        data['db'] = Processos.objects.filter(Materiais_Identificado__icontains=search)
        data['db'] = Processos.objects.filter(Informe_de_Uso__icontains=search)
        data['db'] = Processos.objects.filter(Nota_Fiscal__icontains=search)
        data['db'] = Processos.objects.filter(Setor__icontains=search)
        data['db'] = Processos.objects.filter(Processo__icontains=search)
    else:
        data['db'] = Processos.objects.all()
    all = Processos.objects.all()
    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data ={}
    data['form'] = ProcessosForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProcessosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Processos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Processos.objects.get(pk=pk)
    data['form'] = ProcessosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Processos.objects.get(pk=pk)
    form = ProcessosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Processos.objects.get(pk=pk)
    db.delete()
    return redirect('home')