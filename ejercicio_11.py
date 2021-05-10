"""
Ejercicio 11.
    - Hacer un programa que tenga una lista de números enteros
    - Recorrer la lista y mostrarla
    - Hacer función que recorra listas de números y devuelva un string
    - Ordenar la lista y mostrarla
    - Mostrar su longitud
    - Buscar algún elemento, que el usuario pida por teclado
"""
#Creación de la lista
lista_enteros = [100, 2401, 201, 17, 1019, 2020, 14000]

#Recorrer la lista y mostrarla
print('Recorrer lista')
for i in lista_enteros:
    print(str(i) + ', ', end='')
print('\n')

#Hacer función que recorra listas de números y devuelva un string
#Método 1
print('Función #1 para recorrer listas')
def recorrer_lista_1(lista):
    str_lista = ' '.join(str(x) for x in lista)
    return str_lista

print(recorrer_lista_1(lista_enteros))
print('\n')

#Método 2
print('Función #2 para recorrer listas')
def recorrer_lista_2(lista):
    str_lista = ''
    for i in lista:
        str_lista += str(i) + ' '
    return str_lista

print(recorrer_lista_2(lista_enteros))
print('\n')

#Ordenar lista y mostrarla
print('Lista ordenada')
lista_enteros.sort()
print(lista_enteros)
print('\n')

#Mostrar longitud
print(f'La longitud de la lista es {len(lista_enteros)}')
print('\n')

#Buscar elemento
num_busq = int(input('Ingrese el número que busca: '))
print('\n')

#busqueda método 1
print('Método de búsqueda #1')
encontrado = False
for i in lista_enteros:
    if i == num_busq:
        print(f'Elemento encontrado en el índice {lista_enteros.index(i)}')
        encontrado = True
print(f'Elemento {num_busq} no está en la lista') if encontrado == False else print(end='')
print('\n')

#busqueda método 2
print('Método de búsqueda #2')
if num_busq in lista_enteros:
    print(f'Elemento encontrado en el índice {lista_enteros.index(num_busq)}')
else:
    print(f'Elemento {num_busq} no se encuentra en la lista')