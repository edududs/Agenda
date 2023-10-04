from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse("contact:create")
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            "site_title": "Criando Contato - ",
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            print("Formulário é válido")
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect("contact:update", contact_id=contact.pk)

        return render(request, "contact/create.html", context)

    context = {
        "site_title": "Criando Contato - ",
        "form": ContactForm(),
        "form_action": form_action,
    }

    return render(request, "contact/create.html", context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse("contact:update", args=(contact_id,))
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            "site_title": "Atualizando Contato - ",
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            print("Formulário é válido")
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect("contact:update", contact_id=contact.pk)

        return render(request, "contact/create.html", context)

    context = {
        "site_title": "Atualizando Contato - ",
        "form": ContactForm(instance=contact),
        "form_action": form_action,
    }

    return render(request, "contact/create.html", context)


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get("confirmation", "no")
    context = {
        "contact": contact,
        "site_title": "Deletando Contato - ",
        "confirmation": confirmation,
    }
    print("confirmation", confirmation)
    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index")
    return render(request, "contact/contact.html", context)
