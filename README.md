Aplicação de Registro de Usuários - Django

Esta é uma aplicação simples desenvolvida em Django para registro de usuários. Ela permite que novos usuários se cadastrem, façam login, atualizem seu email e senha, e também excluam suas contas.

Funcionalidades:<br>
Registro de novos usuários com nome, sobrenome, nome de usuário, email e senha.<br>
Login para usuários cadastrados.<br>
Atualização do email associado à conta do usuário.<br>
Atualização da senha do usuário, seguindo critérios de segurança.<br>
Exclusão da conta do usuário.<br><br>
Pré-requisitos:<br>
Python 3.x<br>
Django 3.x<br><br>
Instruções de Uso:<br>
Clone o repositório para o seu ambiente local.<br>
Instale as dependências necessárias através do comando pip install -r requirements.txt.<br>
Execute as migrações do banco de dados através do comando python manage.py migrate.<br>
Crie um superusuário para acessar o painel de administração com o comando python manage.py createsuperuser.<br>
Inicie o servidor de desenvolvimento com o comando python manage.py runserver.<br>
Acesse a aplicação no seu navegador através do endereço http://localhost:8000/.<br><br>
Observações:<br>
Certifique-se de ter o Python e o Django instalados em seu ambiente local antes de executar a aplicação.<br>
O arquivo requirements.txt contém todas as dependências necessárias para o projeto.<br>
O arquivo db.sqlite3 armazenará os dados do banco de dados local.<br>
Utilize a página de registro para criar novos usuários e a página de login para acessar a área de dashboard.<br>
Na área de dashboard, os usuários podem atualizar seu email e senha, e também excluir sua conta.<br>
O painel de administração pode ser acessado através do endereço http://localhost:8000/admin/ após criar o superusuário.<br>

Autor:
João Vitor Ruiz
minuano95@gmail.com
