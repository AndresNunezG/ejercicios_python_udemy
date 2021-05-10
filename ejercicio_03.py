"""
Ejercicio 3.
    - Escribir un script con el ciclo while y con el ciclo for que muestre
      los cuadrados de los 60 primeros números naturales [1 - 60]
"""

#Solución 1 - Ciclo while
print('Con el ciclo While')
i = 1
while i < 61:
    print(str(i ** 2) + '-', end = '') #Tambien se puede usar la exp. (i * i)
    i +=  1
print('')

#Solución 1 - Ciclo for
print('Con el ciclo For')
for j in range(1, 61):
    print(str(pow(j, 2)) + '-', end = '') #pow() para elevar en otras bases también
print('')

#Solución 3 - Con list comprehension
print('Con list comprehension')
lista = [(k * k) for k in range(1, 61)]
print(lista)
