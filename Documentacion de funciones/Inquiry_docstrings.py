def inquirys(request):
   
    """
        Esta funcion hace que un usuario pueda solicitar un servicio publicado en la pagina y se pueda contactar con la persona que
        esta publicando el servicio.
        
        Se cuenta con 4 campos con la informacion del usuario y 1 que muestra el servicio a solicitar 
        (listing*, 
        username*, 
        email*, 
        phone, 
        message),

        Las variables marcadas (*) son aquellas que se rellenan automaticamente con la informacion del usuario y del servicio.

        Una vez rellenado los campos es posible utilizar un boton "Send" para enviarle un correo a la persona que publico que 
        su servicio esta siendo solicitado.
        
    """