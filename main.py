# Este código servirá para generar contraseñas aleatorias 
# El usuario podrá elegir la longitud de la contraseña
# El usuario podrá elegir si la contraseña tendrá letras mayúsculas, minúsculas, números y/o símbolos

import random
import string
import datetime
import pandas as pd
import os


def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    try:
        # Conjuntos de caracteres disponibles
        caracteres = ''
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_simbolos:
            caracteres += string.punctuation

        # Verificar que haya al menos un conjunto de caracteres seleccionado
        if not caracteres:
            raise ValueError("Debe seleccionar al menos un conjunto de caracteres.")

        # Verificar que la longitud sea mayor a cero
        if longitud <= 0:
            raise ValueError("La longitud de la contraseña debe ser mayor a cero.")

        # Generar la contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        return contraseña

    except ValueError as e:
        print(f"Error: {str(e)}")
        return None

def guardar_contraseña(contraseña):
    try:
        ahora = datetime.datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
        nombre = input("Nombre para la contraseña: ")
        data = {'FECHA': [fecha_hora], 'NOMBRE CONTRASEÑA': [nombre], 'CONTRASEÑA': [contraseña]}
        df = pd.DataFrame(data)
        if os.path.isfile('contraseñas_guardadas.xlsx'):
            with pd.ExcelWriter('contraseñas_guardadas.xlsx', engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, index=False, header=False)
        else:
            df.to_excel('contraseñas_guardadas.xlsx', index=False)
        print("Contraseña guardada con éxito. Viva! Viva! Viva!")
    except Exception as e:
        print(f"Error al guardar la contraseña: {str(e)}")     


def main():
    print("""
#############################
# Yeyo's Password Generator #
#############################
""")
    while True:
        try:
            longitud = input('Longitud de la contraseña: ')
            while not longitud.isdigit() or int(longitud) <= 0 or int(longitud) > 100:
                print("La longitud de la contraseña debe ser un número mayor a cero y menor o igual a 100.")
                longitud = input('Longitud de la contraseña: ')
            longitud = int(longitud)
            
            incluir_mayusculas = ''
            while incluir_mayusculas != 's' and incluir_mayusculas != 'n':
                incluir_mayusculas = input('¿Incluir mayúsculas? (s/n): ').lower()
            
            incluir_minusculas = ''
            while incluir_minusculas != 's' and incluir_minusculas != 'n':
                incluir_minusculas = input('¿Incluir minúsculas? (s/n): ').lower()
            
            incluir_numeros = ''
            while incluir_numeros != 's' and incluir_numeros != 'n':
                incluir_numeros = input('¿Incluir números? (s/n): ').lower()
            
            incluir_simbolos = ''
            while incluir_simbolos != 's' and incluir_simbolos != 'n':
                incluir_simbolos = input('¿Incluir símbolos? (s/n): ').lower() 
                
            if incluir_mayusculas == 'n' and incluir_minusculas == 'n' and incluir_numeros == 'n' and incluir_simbolos == 'n':
                print("Debe seleccionar al menos un conjunto de caracteres.")
                continue
            
            if incluir_mayusculas == 's':
                incluir_mayusculas = True
            else:
                incluir_mayusculas = False
                
            if incluir_minusculas == 's':
                incluir_minusculas = True
            else:
                incluir_minusculas = False
            
            if incluir_numeros == 's':
                incluir_numeros = True
            else:
                incluir_numeros = False
                
            if incluir_simbolos == 's':
                incluir_simbolos = True
            else:
                incluir_simbolos = False


            contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
            print(f'Contraseña generada: {contraseña}')

            guardar = ''
            while guardar != 's' and guardar != 'n':
                guardar = input("¿Deseas guardar la contraseña generada? (s/n): ").lower()
            if guardar == 's':
                guardar_contraseña(contraseña)
                
            continuar = ''
            while continuar != 's' and continuar != 'n':
                continuar = input("¿Deseas generar otra contraseña? (s/n): ").lower()
            if continuar == 'n':
                print("Bye bye!")
                break

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

    
if __name__ == '__main__':
    main()
    