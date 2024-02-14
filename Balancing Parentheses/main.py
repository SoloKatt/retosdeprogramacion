import math
import os
import random
import re
import sys

#La función esta esperando regresar un ENTERO (INTEGER).
#La función acepta una cadena (STRING) s como parametro.

#Funcion: obtener el minimo para balancear los paréntesis. 
def getMin(cadena):

    #Mantener el balance de la cadena
    balance = 0
    cantidad_faltante = 0

    #Iterar sobre cada carácter en la cadena
    for i in range (0, len(cadena)):
        #Si encontramos un '(' aumentamos el balance
        if (cadena[i] == '('):
            balance += 1
        else:
            #Si encontramos un ')' disminuimos el balance
            balance -= 1
        
        #Si el balance llega a -1 significa que hay un ')' sin su correspondiente '('
        if (balance == -1):
            #Incrementamos la cantidad de '(' faltantes
            cantidad_faltante += 1
            #Ajustamos el balance sumando 1
            balance += 1
    
    #Retornamos el balance actual más la cantidad de '(' faltantes
    return balance + cantidad_faltante

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    cadena = input("Ingresar la cadena de paréntesis '()': ")
    #cadena = '(((())'
    minimo_para_balancear =  getMin(cadena)
    print(f"El mínimo para balancear los paréntesis en la cadena '{cadena}' es: {minimo_para_balancear}")
    #fptr.write(str(resultado) + '\n')
    #fptr.close()