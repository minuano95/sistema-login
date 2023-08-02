from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EmailForm(forms.Form):
    """
    Um formulário simples para atualização de email.

    Este formulário permite que os usuários atualizem seu endereço de email,
    verificando se o novo email já está em uso por outro usuário.

    Campos:
        email (EmailField): O novo endereço de email do usuário.

    Métodos:
        clean_email: Verifica se o email fornecido já está em uso por outro usuário.
    """

    email = forms.EmailField(required=True, label='Email')
               
    def clean_email(self):
        """
        Valida o email fornecido e verifica se já está em uso por outro usuário.

        Returns:
            str: O novo endereço de email se válido.

        Raises:
            ValidationError: Se o email fornecido já estiver em uso.
        """
        email = self.cleaned_data.get('email')
        emailExists = User.objects.filter(email=email).exists()
        
        if emailExists:
            raise ValidationError('Esse e-mail já está em uso.')

        return email