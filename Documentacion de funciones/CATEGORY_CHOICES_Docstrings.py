CATEGORY_CHOICES = (
    ('Belleza', 'Belleza'),
)
"""
Category choices es una tupla que contiene tuplas de dos elementos, el primero es el valor que se guarda en la base de datos y el segundo es el valor que se muestra al usuario.
esta tupla es utilizada para crear un campo de tipo ChoiceField en el formulario de creacion de anuncios en la parte de categorias,
este campo es utilizado para que el usuario seleccione la categoria de su anuncio y no pueda pasar un valor que no este en la tupla
"""