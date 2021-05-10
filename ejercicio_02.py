"""
Ejercicio 2.
    - Escribir un script que muestre en pantalla todos lo números pares del 1 al 50.
"""

#Solución 1
#Utilizando un ciclo for y validación

for i in range(50 + 1):
    if i % 2 == 0:
        print(str(i) + '-' , end='')
print('')

#Solución 2
#Utilizando list comprehension con condicionales

lista = [j for j in range(51) if j % 2 == 0] # [expresión for item in lista condicional
print(lista)