from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    # Aqui, a gente sobrescreve o __init__, que é o método de inicialização do formulário.
    def __init__(self, *args, **kwargs):
        # Primeiro, chamamos o __init__ original da classe pai (forms.ModelForm), porque ele faz as coisas básicas.
        super(UserForm, self).__init__(*args, **kwargs)

        # Agora, para cada campo do formulário, a gente vai adicionar uma classe 'form-control'.
        # Isso é basicamente uma maneira de estilizar automaticamente todos os inputs com o Bootstrap.
        for field in self.fields.values():
            # A gente acessa o 'widget' de cada campo (o HTML do campo, tipo <input>, <textarea>, etc.)
            # E atualiza ele, colocando a classe 'form-control' (do Bootstrap) pra ele ficar estilizado.
            field.widget.attrs.update({'class': 'form-control'})