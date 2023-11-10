from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
<<<<<<< HEAD

def logout_view(request):
    logout(request)
    return redirect("index")
=======
def home_view(request):
    return render(request, "home.html")
>>>>>>> 796bd902aeab841c3926976a4886b744bd086395
