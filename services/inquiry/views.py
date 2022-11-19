from django.shortcuts import render, redirect
from django.contrib import messages
from .models import inquiry
from django.core.mail import send_mail

def inquirys(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        owner_mail = request.POST['owner_mail']
        owner_id = request.POST['owner_id']
    
        if request.user.is_authenticated:
            user_id  = request.user.id
            has_inquired = inquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_inquired:
                messages.error(request, 'Ya ha realizado una solicitud para este servicio.')
                return redirect('/listings/'+listing_id+'/')
            inquirys1 = inquiry(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id, owner_id=owner_id)
            inquirys1.save()
            send_mail(
                'Solicitud de '+ listing,
                'Ha habido una solicitud para '+ listing +'.Inicie sesion para obtener mas informacion',
                'correo@gmail.com',
                [owner_mail],
                fail_silently=False
            )
            messages.success(request, "Su solicitud ha sido realizada, el propietario de la publicación se comunicará con usted lo antes posible")
            return redirect('/listings/'+listing_id+'/')