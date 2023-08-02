from django import forms

class LoginForm(forms.Form):
    """
    Um formulário simples para autenticação de usuário.

    Este formulário permite que os usuários façam login fornecendo seu nome de usuário e senha.

    Campos:
        username (CharField): O nome de usuário do usuário.
        password (CharField): A senha do usuário.

    Atributos:
        Nenhum atributo específico neste formulário.

    Métodos:
        Nenhum método específico neste formulário.
    """

    username = forms.CharField(label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
