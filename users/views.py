from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForms
from django.contrib.auth.models import User

def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,'\n', password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/landing/')
        #    context = {"error": "Something Wrong!"}
        else:
            login(request, user)
            return redirect('/admin/')
    return render(request, "accounts/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, "accounts/logout.html", {})


def sign_up(request):
    error_message = None
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                User.objects.get(username=username)
                error_message = "Username already exists. Please choose a different one."
            except User.DoesNotExist:
                form.save()
                return redirect('/')
    else:
        form = SignUpForms()
    return render(request, 'accounts/signup.html', {'form': form, 'error_message': error_message})
