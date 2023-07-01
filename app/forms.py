from django.forms import ModelForm
from app.models import Processos

# Create the form class.
class ProcessosForm(ModelForm):
    class Meta:
        model = Processos
        fields = ['Protocolo', 'Status', 'Paciente', 'Materiais_Identificado', 'Informe_de_Uso', 'Nota_Fiscal', 'Setor', 'Processo']