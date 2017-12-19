from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login_view(request):
    error = False

    if not request.user.is_authenticated :
        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)  # Nous vérifions si les données sont correctes
                if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # nous connectons l'utilisateur
                else: # sinon une erreur sera affichée
                    error = True
        else:
            form = ConnexionForm()
        return render(request, 'accounts/login.html', locals())
    else:
        return redirect(index)

@login_required()
def index(request) :
    if request.user.is_authenticated :
        print("Authenticated")
    else :
        return render(request, 'accounts/connexion.html', locals())

    return render(request, 'accounts/index.html', locals())

def logoutview(request):
    logout(request)
    return redirect(reverse(login_view))