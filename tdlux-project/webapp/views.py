from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Product, User
from .forms import UserForm

def index(request):
    products = Product.objects.all().distinct()
    
    context = {"products": products}
    return render(request, "index.html", context=context)

def login(request):
    return render(request, "login.html")
    
def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
        return HttpResponseRedirect("/")
    else:
        userform = UserForm()
   
    return render(request, "register.html", {'userform': userform})

def cart(request):
    return render(request, "cart.html")
    