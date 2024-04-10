from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .models import Agendamento
from .forms import ScheduleForm


def bahia(request): 
    return HttpResponse('Tá perdido amigão a bahia fica pra lá>>>>>>>')

    
def criar_agendamento(request):
    if request.method == 'POST':
        form = ScheduleForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else: 
        form = ScheduleForm()
    return render(request, 'criar_agendamento.html', {'form':form})

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamentos':agendamentos})

def confirmar_agendamento(request):
    if request.method == 'POST':
        form = ScheduleForm (request.POST) 
        if form.is_valid():
            agendamento = form.save()
            agendamento.status = 'CONFIRMADO'
            agendamento.save()
            return redirect(request, 'confirmar_agendamento.html', {'form':form})
    else:
        form = ScheduleForm()
    return render('confirmar_agendamento.html', {'form':form})

def pagina_confirmacao(request, agendamento_id):
    agendamento = Agendamento.objects.get(id = agendamento_id)
    return render(request, 'confirmar_agendamento.html', {'agendamento':agendamento})
    
    
            
            