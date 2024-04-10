from django.db import models # type: ignore

class Agendamento(models.Model): 
    hora = models.TimeField(default='08:00:00')
    data = models.DateField(default='2020-01-01')
    descricao = models.TextField()
    titulo = models.CharField(max_length=50, default='Reserva de Agendamento')
    cliente = models.CharField(max_length=50, default = ' ')
    profissional = models.CharField(max_length=50, default = ' ')
    status = models.CharField(max_length=8, default = 'PENDENTE')
    
     