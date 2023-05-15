from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Product, User
from .forms import UserForm, LoginForm
from django.contrib.auth import logout, authenticate, login

def index(request):
    products = Product.objects.all().distinct()
    
    context = {"products": products}
    return render(request, "index.html", context=context)

    
def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        
        for field in userform:
            if field.errors.__len__() > 0:
                print("Field Error:", field.name,  field.errors)
                

        if userform.is_valid():
            
            user = userform.save()
            return HttpResponseRedirect("/")
    else:
        userform = UserForm()
   
    return render(request, "register.html", {'userform': userform})

def cart(request):
    return render(request, "cart.html")

def logout_v(request):
    logout(request)
    return redirect("/")
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    form.add_error("username", ValidationError("Аккаунт заблокирован"))
            else:
                form.add_error("username", ValidationError("Неверный логин или пароль"))
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})