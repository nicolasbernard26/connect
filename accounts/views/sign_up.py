from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from ..forms import ProfileForm, UserComplementForm
from django.contrib.auth.decorators import login_required

from .profile import profile_view

def sign_up_view(request):
    error = False

    if request.method == 'POST':
        forms=[UserCreationForm(request.POST or None), UserComplementForm(request.POST or None), ProfileForm(request.POST or None, request.FILES)]

        if forms[0].is_valid() and forms[1].is_valid() and forms[2].is_valid(): 
            envoi = True
            profile = forms[2].save(commit=False)  # Ne sauvegarde pas directement l'article dans la base de données
            user = forms[0].save(commit=False)
            user.email = forms[1].cleaned_data["email"]
            user.first_name = forms[1].cleaned_data["first_name"]
            user.last_name = forms[1].cleaned_data["last_name"]
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')    

            profile.user = user
            profile.save()

            return redirect(profile_view)

    else:
        forms=[UserCreationForm(), UserComplementForm(), ProfileForm()]
    return render(request, 'accounts/signup.html', locals())
