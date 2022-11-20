from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, **extrafields):
        if not username:
            raise ValueError('Se debe tener un nombre de usuario')
        user = self.model(username=username, email=self.normalize_email(email), **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, password, email=None):
        user = self.create_user(username, email, password)
        user.is_staff =True
        user.is_superuser = True
        user.save(using=self._db)
 
        return user

   

class User(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=30)
    apellidoP = models.CharField(max_length=20)
    apellidoM = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    fechaDeNacimiento = models.DateField
    password = models.CharField(max_length=100)
    telefono = models.BigIntegerField(default=0)
    favourites = models.CharField(max_length=200,default='')
    rate_listing = models.CharField(max_length=200,default='')#Borrar este campo p
    direccion = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'username'