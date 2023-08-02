import re
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PasswordForm(ModelForm):
    """
    Um formulário para alteração de senha do usuário.

    Este formulário permite que os usuários atualizem sua senha, verificando se a nova senha
    atende aos requisitos de segurança (mínimo de 8 caracteres, com pelo menos uma letra maiúscula,
    uma letra minúscula e um número).

    Campos:
        password (CharField): A nova senha do usuário.
        password2 (CharField): A confirmação da nova senha do usuário.

    Métodos:
        validatePassword(password): Valida a nova senha de acordo com os critérios de segurança.
        clean(): Executa a validação do formulário e verifica se as senhas são iguais.

    Atributos:
        Nenhum atributo específico neste formulário.
    """

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmar nova senha'
    )   

    class Meta:
        model = User 
        fields = ['password', 'password2']
        widgets = {
            'password': forms.PasswordInput(), 
        } 
        labels = {
            'password': 'Nova senha'
        }
    
    def validatePassword(self, password):
        """
        Valida a nova senha de acordo com os critérios de segurança.

        Args:
            password (str): A nova senha a ser validada.

        Raises:
            ValidationError: Se a senha não atender aos requisitos de segurança.
        """
        expression = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
        if not expression.match(password):
            raise ValidationError(
                {'password': "A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número. O comprimento deve ser de pelo menos 8 caracteres."
                 })
        
        return password
    
    def clean(self):
        """
        Executa a validação do formulário e verifica se as senhas são iguais.

        Returns:
            dict: Os dados validados do formulário.

        Raises:
            ValidationError: Se as senhas fornecidas não forem iguais.
        """
        data = super().clean()
        password = data.get('password', None)
        password2 = data.get('password2', None)
 
        if password is None or len(password) < 8:
            raise ValidationError({
                'password': 'A senha é muito curta.'
            })
            
        self.validatePassword(password)
        
        if password != password2:
            raise ValidationError({
                'password': 'As senhas devem ser iguais.',
                'password2': 'As senhas devem ser iguais.'
                })
            
        return data
