from django.shortcuts import render

def login_view(request):
    return render(request, 'auth/login.html')

def signup_view(request):
    return render(request, 'auth/signup.html')