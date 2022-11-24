def listings(request):
    """Esta funcion es utilizada para mostrar los anuncios en la pagina de publicaciones destacadas (listings.html)
    , estos anuncios contienen informacion como categoria, proveedor, titulo, celular y correo electronico. 
    """
    #Funcion realizada por Antonio Hernandez y Jared Gonzalez
def listing(request, pk):
    """Esta funcion es utilizada para mostrar los anuncios en la pagina de publicaciones destacadas (listing.html)
    , estos anuncios contienen informacion como el titulo, la descripcion, el precio, la categoria, la fecha de publicacion, nombre 
     del vendedor, la direccion, el numero de telefono, el correo electronico y la imagen o imagenes del anuncio. 

      Favoritos
    En esta funcion tambien se maneja la funcion de favoritos, donde el usuario podra agregar las publicaciones de su interes por medio del boton "Agregar a favoritos"
    al momento de agregar una publicacion a favoritos esta se podra encontrar en el dashboard del usuario y el boton pasara a ser "Eliminar de favoritos" donde podra
    eliminar la publicacion si ya no la necesita.

    Rating
    El rating es un valor numerico entre 1 y 10 el cual sera almacenado en la BD y sera promediado entre la cantidad total de usuarios que han valorado la publicacion.
    Si el usuario valoro la publicacion, este no podra valorarla nuevamente con su cuenta. Al momento de valorarla se actualizara el promedio de su rating a la vez que se 
    mostrara en la descripcion del producto cuantos usuarios la han valorado.
    """
    #Funcion realizada por Antonio Hernandez , Jared Gonzalez y Alexis Garcia
def search(request):
    """Esta funcion es utilizada para buscar los anuncios en la pagina de publicaciones destacadas (search.html)
    , estas busquedas son realizadas por medio de palabras claves(descriptions), categoria(category_choices) 
    y precio(price_choices) o ratings(valoraciones por usuarios).
    """
    #Funcion realizada por Antonio Hernandez

def create(request):
    """

    La funcion create consiste en detectar si un usuario en el dashboard preciono "Crear publicacion" al momento de precionar esta boton se llamara a la funcion
    la cual renderizara un fomrulario con los datos necesarios para crear la publicacion, al finalizar de ingresar los datos y crear la publicacion se guardaran los datos 
    en la BD, lo cual generara la publicacion y redirecionara al usuario hacia el dashboard nuevamente.

    """
    #Funcion realizada por Antonio Hernandez
 
def update(request,pk):
    """

    Despues de crear una publicacion se habilitara la opcion de actualizar publicacion, la cual consiste en llamar la informacion que contiene la publicacion que se 
    selecciono, al momento de presionar actualizar se mostraran los datos que contiene y se podran modificar los diversos valores que se muestran. Al finalizar la edicion 
    se guardaran los datos, se actualizara la publicacion y se redireccionara al usuario a su dashboard nuevamente.

    """
    #Funcion realizada por Antonio Hernandez

def delete_listing(request,pk):
    """

    La funcion de borrar publicaciones se puede llamar desde el dashboard en la seccion de las publicaciones al usarla eliminara la publicacion indicada.

    """
    #Funcion realizada por Antonio Hernandez

def comments(request,pk):
    """

    Esta funcion no se encuentra totalmente funcional. 

    COnsiste en poder publicar un comentario luego de hacer un rating. Se llevara al usuario a un formulario donde podra ingresar un comentario a su gusto y este sera visible 
    en la publicacion que se hizo, al finalizar el formulario se le redirecionara hacia el inicio de las publicaciones.

    """
    #Funcion realizada por Alexis Garcia




