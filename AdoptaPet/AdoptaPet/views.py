#importo las clasesd de Django
from AdoptaPet.forms import RegisterForm
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages



#Defino funciones que luego asocio con las urls

#Vista INDEX
def index(request):
    return render(request, 'index.html', {
        'message': 'Listado de Productos', 
        'title': 'Productos',
        'products': [
                {'title':'Remera', 'price': 5, 'stock': True},
                {'title':'Camisa', 'price': 7, 'stock': True},
                {'title':'Mochila', 'price': 20, 'stock': False},
            
            ]
        })

#Vista de LOGEO USUARIOS
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user: 
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, 'users/login.html', {

    })

#Vista de DESLOGEO USUARIOS
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

#Vista de REGISTRO USUARIOS
def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })

