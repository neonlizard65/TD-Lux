from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")
    
def register(request):
    return render(request, "register.html")

def cart(request):
    return render(request, "cart.html")
    