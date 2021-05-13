"""
Ejericio 16.
    - Solicitar al usuario un texto o cadena de caracteres
    - Devolver en pantalla el texto de entrada al revés:
    Ej:
    Entrada: 'hola'
    Salida: 'aloh'
"""

#Solicitar texto al usuario
print('Ingrese el texto a ser invertido!')
texto = input('')

#Invertir el texto

#Método 1.
texto_inv = texto[::-1]
print('El texto invertido mediante el método 1 es: ', texto_inv)
print('\n')

#Método 2.
texto_inv = ''
for letra in texto:
    texto_inv = letra + texto_inv

print('El texto invertido mediante el método 2 es: ', texto_inv)
print('\n')