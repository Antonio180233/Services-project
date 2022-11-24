class listings():
    """
    Esta clase contiene los modelos de la tabla listings de la base de datos
    , contiene los campos: 
    owner es el usuario que crea el anuncio
    , title es el titulo del anuncio
    , category es la categoria del anuncio
    , address es la direccion del anuncio
    , city es la ciudad del anuncio
    , state es el estado del anuncio, aunque el campo no es usado, se preevee usarlo en un futuro
    , zipcode para el codigo postal del anuncio
    , description es la descripcion del anuncio
    , price es el precio del anuncio, por defecto es 100MXN, esto se encuentra detallado en la pagina de politicas.

    photo_main, photo_1 es la foto principal del anuncio
    , photo_2, photo_3, photo_4, photo_5, photo_6, 
    is_published, es un booleano que indica si el anuncio esta publicado o no

    list_date es la fecha de creacion del anuncio, en este caso se usa la fecha actual por default
    """
    
    
   #funcion realizada por Jared Gonzalez
