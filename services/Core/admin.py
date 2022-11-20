from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.utils.translation import gettext as _

from Core import models

# Register your models here.

class UserAdmin(BaseUser):
    ordering = ['id']
    list_display = ['id','username', 'email', 'nombre']
    list_display_links = ['id', 'username']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Info personal'),{'fields': ('nombre','apellidoP','apellidoM','telefono','direccion','favourites')}),#borrar tipo de cuenta
        (_('Permisos'), {'fields': ('is_active','is_staff','is_superuser')})
    )
    add_fieldsets = [
        (None,{
            'classes': ('wide',),
            'fields': ('username','email','telefono', 'password1', 'password2')
        })
    ]

admin.site.register(models.User, UserAdmin)