from datetime import timedelta, datetime
from django import forms
from .models import Agendamento
    

class ScheduleForm(forms.ModelForm):
    hora = forms.ChoiceField(choices=[('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        hoje = datetime.now().date()    

        opcoes_data = []

        for i in range(6):
            data = hoje + timedelta(days=i)
            opcoes_data.append((data, data.strftime('%Y-%m-%d')))

        self.fields['data'] = forms.ChoiceField(choices=opcoes_data)

        #self.fields['titulo'].widget.attrs['readonly'] = True 

    class Meta:
        model = Agendamento
        fields = ['cliente', 'profissional', 'descricao',  'data', 'hora']