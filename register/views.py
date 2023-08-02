# Importações necessárias
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from .forms import RegisterForm, LoginForm, EmailForm, PasswordForm

# View para renderizar o formulário de registro
def registerView(request):
    formData = request.session.get('form_data', None)
    form = RegisterForm(formData)
    return render(request, 'register/register.html', context={'form': form})

# View para processar o formulário de registro
def registerCreate(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        userData = form.save(commit=False)
        userData.set_password(userData.password)
        userData.save()
        messages.success(request, 'O seu usuário foi criado com sucesso. Agora você pode fazer login.')
        del(request.session['form_data'])
        return redirect(reverse('register:login'))

    return redirect('register:register')

# View para renderizar o formulário de login
def loginView(request):
    form = LoginForm()
    return render(request, 'register/login.html', {'form': form, 'action': 'register:login_create'})

# View para processar o formulário de login
def loginCreate(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    if form.is_valid():
        is_authenticated = authenticate(username=form.cleaned_data.get('username', ''), password=form.cleaned_data.get('password', ''))
        if is_authenticated is not None:
            login(request, is_authenticated)
            return redirect(reverse('register:dashboard'))
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        messages.error('Usuário ou senha inválidos.')
    return redirect(reverse('register:login'))

# View para fazer logout do usuário
@login_required(login_url='register:login', redirect_field_name='next')
def logoutView(request):
    logout(request)
    return redirect(reverse('register:login'))

# View da página de dashboard (requer autenticação)
@login_required(login_url='register:login', redirect_field_name='next')
def dashboardView(request):
    return render(request, 'register/dashboard.html')

# View para renderizar o formulário de atualização de email (requer autenticação)
@login_required(login_url='register:login', redirect_field_name='next')
def emailUpdateView(request):
    formData = request.session.get('form_data', None)
    form = EmailForm(formData)
    return render(request, 'register/update_email.html', {'form': form})

# View para processar o formulário de atualização de email (requer autenticação)
def emailUpdateViewCreate(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['form_data'] = POST
    form = EmailForm(POST)

    if form.is_valid():
        user = request.user
        novoEmail = form.cleaned_data.get('email')
        user.email = novoEmail
        user.save()
        messages.success(request, 'Seu email foi atualizado com sucesso.')
        return redirect('register:dashboard')

    return redirect('register:update_email')

# View para renderizar o formulário de atualização de senha (requer autenticação)
@login_required(login_url='register:login', redirect_field_name='next')
def passwordUpdateView(request):
    formData = request.session.get('form_data', None)
    form = PasswordForm(formData)
    return render(request, 'register/update_password.html', {'form': form})

# View para processar o formulário de atualização de senha (requer autenticação)
@login_required(login_url='register:login', redirect_field_name='next')
def passwordUpdateViewCreate(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['form_data'] = POST
    form = PasswordForm(POST)

    if form.is_valid():
        # Obter o usuário autenticado
        user = request.user
        new_password = form.cleaned_data.get('password')
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Sua senha foi atualizada com sucesso! Faça o login novamente.')
        logout(request)
        return redirect('register:dashboard')

    return redirect('register:update_password')

@login_required(login_url='register:login', redirect_field_name='next')
def deleteAccountView(request):
    # Obter o usuário autenticado
    user = request.user
    user.delete()
    logout(request)
    messages.success(request, 'Sua conta foi excluída com sucesso. Até logo!')
    return redirect(reverse('register:login'))
