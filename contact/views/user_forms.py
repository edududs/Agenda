from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect("contact:index")

    context = {"site_title": "Criando Contato - ", "form": form}
    return render(request, "contact/register.html", context)


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(
                request, f"Bem-vindo {user.first_name}!\nLogado com sucesso!"
            )
            return redirect("contact:index")
        messages.error(request, "Erro ao logar")

    context = {"site_title": "Login - ", "form": form}

    return render(request, "contact/login.html", context)


@login_required(login_url="contact:login")
def logout_view(request):
    auth.logout(request)
    messages.success(request, "Você foi deslogado com sucesso!")
    return redirect("contact:login")


@login_required(login_url="contact:login")
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != "POST":
        context = {"site_title": "Atualizando Contato - ", "form": form}
        return render(request, "contact/register.html", context)

    form = RegisterUpdateForm(request.POST, instance=request.user)

    if not form.is_valid():
        context = {"site_title": "Atualizando Contato - ", "form": form}
        messages.error(request, "Erro ao atualizar o usuário, o formulário não é válido!")
        return render(request, "contact/register.html", context)
    form.save()
    messages.success(request, "Usuário atualizado com sucesso!")
    return redirect("contact:user_update")
