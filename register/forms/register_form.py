import re
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(ModelForm):
    """
    Um formulário de registro de usuário.

    Este formulário permite que os usuários se registrem fornecendo informações como 
    nome, sobrenome, nome de usuário, e-mail e senha.

    Campos:
        first_name (CharField): Nome do usuário.
        last_name (CharField): Sobrenome do usuário.
        username (CharField): Nome de usuário exclusivo.
        email (EmailField): Endereço de e-mail do usuário.
        password (CharField): Senha do usuário.
        password2 (CharField): Confirmação da senha do usuário.

    Métodos:
        clean_email(): Valida se o e-mail fornecido já está em uso.
        validatePassword(password): Valida a senha de acordo com os critérios de segurança.
        clean(): Executa a validação do formulário e verifica se as senhas são iguais.

    Atributos:
        Nenhum atributo específico neste formulário.
    """

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmar senha'
    )

    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Inicializa o formulário e define todos os campos como obrigatórios.

        O campo 'password' também recebe uma mensagem de ajuda indicando os requisitos de senha.
        """
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
            
            # Password field
            self.fields['password'].help_text = "A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número. O comprimento deve ser de pelo menos 8 caracteres."        
    
    def clean_email(self):
        """
        Valida se o e-mail fornecido já está em uso.

        Raises:
            ValidationError: Se o e-mail já estiver em uso.
        """
        email = self.cleaned_data.get('email')
        emailExists = User.objects.filter(email=email).exists()
        
        if emailExists:
            raise ValidationError('Esse e-mail já está em uso.')
  
    def validatePassword(self, password):
        """
        Valida a senha de acordo com os critérios de segurança.

        Args:
            password (str): A senha a ser validada.

        Raises:
            ValidationError: Se a senha não atender aos critérios de segurança.
        """
        expression = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
        if not expression.match(password):
            raise ValidationError(
                {'password': "A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número. O comprimento deve ser de pelo menos 8 caracteres."
                 })
    
    def clean(self):
        """
        Executa a validação do formulário e verifica se as senhas são iguais.

        Returns:
            dict: Os dados validados do formulário.

        Raises:
            ValidationError: Se as senhas fornecidas não forem iguais ou não atenderem aos critérios de segurança.
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
