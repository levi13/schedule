from django.http import HttpResponse # type: ignore
from django.shortcuts import get_object_or_404, render, redirect
from .models import Agendamento
from .forms import ScheduleForm


def bahia(request): 
    return HttpResponse('Tá perdido amigão a bahia fica pra lá>>>>>>>')

    
def criar_agendamento(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            agendamento = form.save()
            return redirect('pagina_confirmacao', agendamento_id=agendamento.id)  # Remova esta linha
    else:
        form = ScheduleForm()
    return render(request, 'criar_agendamento.html', {'form': form})


def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamentos':agendamentos})

def confirmar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'GET':
        agendamento.status = 'CONFIRMADO'
        agendamento.save()
    return render(request, 'confirmar_agendamento.html', {'agendamento': agendamento})

def pagina_confirmacao(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        agendamento.status = 'CONFIRMADO'
        agendamento.save()
        return redirect('pagina_confirmacao', agendamento_id=agendamento.id) 
    return render(request, 'pagina_confirmacao.html', {'agendamento': agendamento})

