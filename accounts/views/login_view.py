from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
from django.contrib.auth.decorators import login_required

from .my_profile_view import my_profile_view

def login_view(request):
    error = False

    if not request.user.is_authenticated :
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)  # Nous vérifions si les données sont correctes
                if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # nous connectons l'utilisateur
                    profile = user.profile_user
                    return redirect(my_profile_view)
                    
                else: # sinon une erreur sera affichée
                    error = True
        else:
            form = LoginForm()
    return render(request, 'accounts/login.html', locals())
    

@login_required()
def index(request) :
    return render(request, 'accounts/index.html', locals())

