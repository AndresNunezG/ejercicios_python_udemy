"""
Ejercicio 17.
    - Escribir una lista que encuentre el menor número de una lista
"""

#Lista a determinar el menor elemento
lista = [12, 20, 17, 21, -16, 21, 2.0, -2.3, 0]

#Determinar menor elemento
def lista_menor(lista):
    min_elem = 10e6
    indice = 0
    for ind, num in enumerate(lista):
        if num < min_elem:
            min_elem = num
            indice = ind
    return (min_elem, indice)

menor, indice = lista_menor(lista)

print(f'De la lista {lista}')
print(f'El menor elemento es {menor}, en la posición {indice + 1}')

#También se puede usar el método min()
print('El elemento mínimo de la lista es: ', min(lista))