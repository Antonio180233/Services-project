from django.shortcuts import render, redirect, get_object_or_404
from Core.models import User
from listings.models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from inquiry.models import inquiry


import random
import string

estado = False
estado2 = "off"

def randomString(stringLenght=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLenght))

code = randomString()

def register(request):
    if request.method =='POST':
        nombre = request.POST['nombre']
        apellidoP = request.POST['apellidoP']
        apellidoM = request.POST['apellidoM']
        email = request.POST['email']
        username = request.POST['username']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        password = request.POST['password']
        password2 = request.POST['password2']


        user = User

        context = {
            'nombre': nombre,
            'apellidoP': apellidoP,
            'apellidoM': apellidoM,
            'email': email,
            'username': username,
            'telefono': telefono,
            'direccion': direccion,
            'password': password,
        }

        if password == password2:
            if user.objects.filter(username=username).exists():
                messages.error(request, 'Este nombre de usuario ya existe')
                return redirect('register')

            else:
                if user.objects.filter(email=email).exists():
                    messages.error(request, 'Este correo ya esta en uso')
                    return redirect('register')
                else:
                    if user.objects.filter(telefono=telefono).exists():
                        messages.error(request, 'Este numero de telefono ya esta en uso')
                        return redirect('register')
                    else:
                        send_mail(
                            'Confirmacion de la cuenta',
                            'Hola '+ nombre + 'tu codigo de confirmacion es: '+code,
                            'diamondsoftwaresolutions4@gmail.com',
                            [email],
                            fail_silently = False
                        )
                        request.method = 'GET'
                        return render(request, 'accounts/confirmregister.html',context)
        else:
            messages.error(request, 'Las contrase;as no son iguales')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def confirmregister(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidoP = request.POST['apellidoP']
        apellidoM = request.POST['apellidoM']
        email = request.POST['email']
        username = request.POST['username']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        password = request.POST['password']
        confirmcode = request.POST['confirmcode']
      
        user = User

        context = {
            'nombre': nombre,
            'apellidoP': apellidoP,
            'apellidoM': apellidoM,
            'email': email,
            'username': username,
            'telefono': telefono,
            'direccion': direccion,
            'password': password,
           
        }
        if code == confirmcode:
            user = user.objects.create_user(username=username, email=email, password=password,
            telefono=telefono,nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, direccion=direccion)
            user.save()
            login(request, user)
            messages.success(request, 'Inicio de sesion exitoso')
            return redirect('index')
        else:
            messages.error(request, 'Codigo de confirmacion invalido')
            return render(request, 'accounts/confirmregister.html', context)
    else:
        return redirect('register')        

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesion exitoso')
            return redirect('index')
        else:
            messages.error(request, 'contraseña o usuario incorrecto')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def userlogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Sesion cerrada exitosamente')
        return redirect('login')

@login_required
def dashboard(request):
    mylistings = Listing.objects.order_by('-list_date').filter(owner=request.user)
    context = {
        'listings': mylistings
    }
    return render(request, 'accounts/dashboard.html', context)

def favourite_listing(request):
    favourites = request.user.favourites
    favourites = favourites.split(',')[1:]
    print(favourites)
    listings = []
    for i in favourites:
        listings.append(get_object_or_404(Listing,pk=int(i)))
    context = {
        'listings': listings
    }
    return render(request, 'accounts/favourites.html', context)

@login_required
def myinquiries(request):
    myinquiry= inquiry.objects.all().filter(user_id=request.user.id)
    context = {
        'myinquiries': myinquiry
    }
    return render(request, 'accounts/dashboard_myinquiries.html', context)

@login_required
def inquiry1(request):
    myinquiry= inquiry.objects.all().filter(owner_id=request.user.id)
    context = {
        'inquiries': myinquiry
    }
    return render(request, 'accounts/dashboard_inquiries.html', context)

@login_required
@login_required
def change_password(request):
    if request.method=='POST':
        user = request.user
        currentpassword = request.POST['currentpassword']
        if not check_password(currentpassword,user.password):
            messages.error(request,'Contraseña actual incorrecta')
            return redirect('dashboard')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request,'Se ha cerrado la sesión')
            messages.success(request,'Ha cambiado correctamente la contraseña')
            messages.success(request,'Use su nueva contraseña para iniciar sesión')
        else:
            messages.error(request,'Passwords do not match')
        return redirect('dashboard')
    
    else:
        return render(request,'accounts/change_password.html')
