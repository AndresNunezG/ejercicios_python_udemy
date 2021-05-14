"""
Ejercicio 22.
    - Recibir nombre y apellido del usuario
    - Agregar información recibida al archivo de texto
    - Parar la recepción de nombres si se agrega apellido y/o nombre 'stop! 
"""

import os

#Abrir archivo de texto con permisos de escritura
class formulario_usuarios():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def abrir_archivo(self): #abrir o crear archivo
        if not os.path.isfile(self.nombre_archivo): #validar si el archivo existe
            print(f'¡Archivo {self.nombre_archivo} no encontrado!')
            print(f'Se crea el archivo: {self.nombre_archivo}')
            self.archivo = open(self.nombre_archivo, 'w') #crear si no existe
        else: #si existe, abrir con permiso de 'append'
            self.archivo = open(os.path.abspath(self.nombre_archivo), 'a')
    
    def recibir_escribir(self):
        print('Ingrese la información solicitada.')
        while True:
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            if (nombre == 'stop!') or (apellido == 'stop!'):
                print('Ingreso de datos finalizado.')
                self.archivo.close() #cerrar archivo
                break #parar el ciclo
            self.archivo.write(nombre + ' ')
            self.archivo.write(apellido + '\n')

nombre_archivo = input('Ingrese el nombre del archivo (sin .txt): ')
programa = formulario_usuarios(nombre_archivo + '.txt')
programa.abrir_archivo()
programa.recibir_escribir()