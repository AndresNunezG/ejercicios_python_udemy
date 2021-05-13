"""
Ejercicio 18.
    Escribir una función que devuelva el volumen de una esfera por su radio
    4/3 * pi * r ^ 3
    - Solicitar al usuario el radio de la esfera
    - Calcular el volumen de la esfera
    - Mostrar el resultado
"""

#Solicitar radio al usuario
print('Cálculo del volumen de una esfera')
radio = float(input('Ingrese el radio: '))

#Calcular el radio
#importar el módulo math para obtener pi π
import math 

#crear función
def vol_esfera(radio):
    return ((4/3) * (math.pi)) * pow(radio, 3)

print(f'Una esfera con radio {radio}, tiene un volumen: {vol_esfera(radio)}')