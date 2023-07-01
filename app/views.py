from django.shortcuts import render, redirect
from app.forms import ProcessosForm
from app.models import Processos

# Create your views here.
def home(request):
    data = {}
    data['db'] = Processos.objects.all()
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