from django.forms import ModelForm
from .models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'curso', 'cpf', 'rg', 'data_nascimento', 'data_ingresso']

    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'