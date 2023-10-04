from django.shortcuts import render, redirect
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
