"""
Ejercicio 20.
    - Escribir una función que indique cuantas vocales tiene una palabra
"""

#Solicitar texto al usuario
palabra = input('Ingrese un texto: ')

#Crear función para contar vocales con docstring
def contar_vocales(texto):
    """
    (texto). Entrada a determinar el número de vocales
    función que cuente la cantidad de vocales
    """
    #Declarar lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0 #inicializar contador
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador

print(f'La cantidad de vocales en el texto es: {contar_vocales(palabra)} vocales')