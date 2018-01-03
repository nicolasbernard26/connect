from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import ConnexionForm
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
                    profile = user.profile_user
                    
                else: # sinon une erreur sera affichée
                    error = True
        else:
            form = ConnexionForm()
    return render(request, 'accounts/login.html', locals())
    

@login_required()
def index(request) :
    return render(request, 'accounts/index.html', locals())

def logout_view(request):
    logout(request)
    return redirect(reverse(login_view))