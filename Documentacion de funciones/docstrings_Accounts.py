def randomString(  stringLenght=6):
   """
   Genera un string aleatorio de longitud =6 por default, para ser usado como codigo de verificacion
   , enviando un correo al usuario, para que pueda verificar su cuenta y poder iniciar sesion
   """
def register(request):
    """
    Funcion que se encarga de registrar a un usuario, para poder iniciar sesion en la aplicacion, contiene los campos:
    nombre, apellidoP, apellidoM, email, username, telefono, direccion, password, password2, tipoCuenta,
    tipoCuenta es un booleano que nos dice si el usuario es un cliente o un proveedor,
    si es un cliente, el valor es False, si es un proveedor, el valor es True.
    
    existen condiciones para que el usuario pueda registrarse, si el usuario ya existe, se le notifica al usuario que el username ya existe
    si el correo ya existe, se le notifica al usuario que el correo ya existe, si el telefono ya existe, se le notifica al usuario que el telefono ya existe,
    si el password y el password2 no coinciden, se le notifica al usuario que los passwords no coinciden.

    si los datos son correctos, se envia un correo al usuario con un codigo de verificacion, para que pueda verificar su cuenta y poder iniciar sesion
    el correo es enviado desde la cuenta de gmail: diamondsoftwaresolutions4@gmail.com

   
    si el registro se realizo, se le notifica al usuario que se registro correctamente y se le redirecciona a la pagina de inicio de sesion
    para comenzar a buscar servicios    
    
"""
     #funcion realizada por Alexis Garcia

def confirmregister(request):
    """
    Funcion que se encarga de verificar la cuenta del usuario, para poder iniciar sesion en la aplicacion
    context es un diccionario que contiene los datos del usuario que se esta registrando
    """
      #funcion realizada por Alexis Garcia
def userlogin(request):
    """
    Funcion que se encarga de iniciar sesion al usuario, para poder acceder a la aplicacion
    si el usuario no ingresa su username o su password, se le notifica al usuario que debe ingresar su username y su password
    si el usuario no existe, se le notifica al usuario que el usuario no existe
    si el usuario ingresa mal nombre o contraseña, se le notifica al usuario que el nombre o la contraseña son incorrectos

    """
      #Funcion realizada por Antonio Hernandez
    
def userlogout(request):
    """
    el parametro request es un objeto para acceder a los datos de la peticion que se esta haciendo al servidor
    Funcion que se encarga de cerrar sesion al usuario, para poder salir de la aplicacion
    """
     #Funcion realizada por Antonio Hernandez
     
    
    
    
