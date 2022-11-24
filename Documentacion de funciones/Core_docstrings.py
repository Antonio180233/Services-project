#Models

#modelos creados por Alexis Garcia
class userManager(BaseUserManager):
    """
        Esta clase define las funciones para la administracion de usuarios como los son la creacion de un usuario regular
        (create_user) o un usuario adminsitrador (create_superuser).
    """

def create_user(self, username, email=None, password=None, **extrafields):
    """
        Esta funcion crea un usuario con los datos ingresados en la pagina de registro (register.html) o al momento de
        hacer un registro con la cuenta de Google se creara un usuario con los datos extraidos del registro y regresa
        el usuario creado. 
        Se cuenta con campos que son obligatorios para la creacion del usuario (username, password, email),
        una vez rellenado se asiganaran al usuario creado.
        En el caso de los extrafields son campos extra que pueden o no existir. Estos campos son definidos en la clase user.
    """

def create_superuser(self, username, password, email=None):
    """
        Esta funcion permite la creacion de un usuario con permisos de administrador regresando el usuario con los
        permisos de staff y superuser. 
        El superuser cuenta como campos obligatorios (username, password y email), estos campos
        se le asignaran al usuario creado asi como tambien se activaran sus permisos (is_staff, is_superuser). Estos
        permisos fueron definidos en la clase user
    """

class user(AbstractBaseUser, PermissionsMixin):
    """
        Esta clase define los paremetros para la creacion de los usuarios, asi como asignar los valores por defecto
        o valores unicos que definiran al usuario.
        AbstractBaseUser representa que seran los campos usados para la creacion de un usuario.
        PermissionsMixin general los permisos is_staff y is_superuser.
    """

#Admin

class userAdmin(BaseUser):
    """
        En esta clase se definen los campos que se mostraran en la vista de administrador al inicio (list_display), asi como el orden por el
        cual se mostraran (ordering), los datos personales (fieldsets: Info personal) y los permisos que corresponden a el usuario seleccionado (fieldsets: permisos)
    """
