from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from contact.forms import RegisterForm


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
            print(user)
    
    context = {"site_title": "Login - "}
    
    return render(request, "contact/login.html", context)
