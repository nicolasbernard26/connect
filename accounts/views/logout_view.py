from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .login_view import login_view

@login_required()
def logout_view(request):
    logout(request)
    return redirect(reverse(login_view))