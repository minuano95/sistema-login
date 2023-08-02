from django.urls import path, include
from django.http import HttpResponse
from .views import registerView, registerCreate, loginView, loginCreate, logoutView, emailUpdateView, emailUpdateViewCreate, passwordUpdateView, passwordUpdateViewCreate, dashboardView, deleteAccountView

app_name = 'register'

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('register/', registerView, name='register'),
    path('register/create/', registerCreate, name='register_create'),
    path('login/', loginView, name='login'),
    path('login/create/', loginCreate, name='login_create'),
    path('logout/', logoutView, name='logout'),
    path('update_email/', emailUpdateView, name='update_email'),
    path('update_email/create', emailUpdateViewCreate, name='update_email_create'),
    path('update_password/', passwordUpdateView, name='update_password'),
    path('update_password/create', passwordUpdateViewCreate, name='update_password_create'),
    path('delete/', deleteAccountView, name='delete_account'),
]
