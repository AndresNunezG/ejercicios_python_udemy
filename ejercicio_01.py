"""
Ejercicio1.
    - Crear variables: "pais" y "continente"
    - Mostrar su valor por pantalla (imprimir)
    - Poner un comentario con el tipo de dato
"""

pais = 'Colombia'
continente = 'América del Sur'
anio = 2021

print('País {} del continente {}'.format(pais, continente)) #format(var1, var2)
print(f'El año es {anio}')                                  #Otro tipo de formateo
print('Tipo de dato de continente: %s' %type(pais))         #Formato string %s 
print('Tipo de dato de anio: %s' %type(anio))               #Formato entero %d