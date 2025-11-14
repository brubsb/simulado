from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def login_view(request):
    """
    View responsável pela autenticação de usuários.
    Exibe mensagem clara em caso de erro e redireciona corretamente.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(username=username)
            if usuario.senha == senha:
                # Salva os dados na sessão
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nome'] = usuario.nome
                return redirect('home')
            else:
                messages.error(request, 'Senha incorreta. Tente novamente.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário não encontrado. Verifique o nome de usuário.')

    return render(request, 'usuarios/login.html')


def home_view(request):
    """
    Tela principal do sistema (menu inicial após login).
    Exibe o nome do usuário logado e acessos para produtos e estoque.
    """
    usuario_nome = request.session.get('usuario_nome')
    if not usuario_nome:
        return redirect('login')

    return render(request, 'usuarios/home.html', {'usuario_nome': usuario_nome})


def logout_view(request):
    """
    Faz logout limpando a sessão e redireciona ao login.
    """
    request.session.flush()
    return redirect('login')
