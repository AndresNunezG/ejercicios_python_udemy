"""
Ejercicio 14.
    - Crear una lista con el contenido de la tabla
    - Mostrar la información ordenada
    ACCION  AVENTURA DEPORTES SimRacing
    COD     CRASH    GTSport  GTSport
    PUBG    GOW      FIFA21   AssetoCorsa
    GTA     DBZ      NBA20    RealRacing3
"""

#Organizar la información de la tabla mostrada en una lista de diccionarios
lst_tabla = [
    {'categoria': 'ACCION',
     'titulos': ['COD', 'PUBG', 'GTA']},
    {'categoria': 'AVENTURA',
     'titulos': ['CRASH', 'GOW', 'DBZ']},
    {'categoria': 'DEPORTES',
     'titulos': ['GTSport', 'FIFA21', 'NBA20']},
    {'categoria': 'SimRacing',
     'titulos': ['GTSport', 'AssetoCorsa', 'RealRacing3']}
    ]

#Mostrar información
ancho_categoria = 19 #caracteres de la col. categoria
ancho_titulos = 41 #caracteres de la col. titulos

#imprimir cabecera
print('_____Categoria_____|_________________Titulos_________________|')

#imprimir filas
for dicc in lst_tabla:

    #Categorias
    print(dicc['categoria'], end='')
    len_cat = len(dicc['categoria'])
    for i in range(ancho_categoria - len_cat):
        print(' ', end='')
    print('|', end='')

    #Titulos
    len_titulos = 0
    for titulo in dicc['titulos']:
        print(titulo + ', ', end= '')
        len_titulos += len(titulo) + 2
    for i in range(ancho_titulos - len_titulos):
        print(' ', end='')
    print('|')
