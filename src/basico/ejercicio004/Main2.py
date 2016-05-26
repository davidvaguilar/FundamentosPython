'''
Created on 17-05-2016

@author: David
'''

def sumar(a,b):
    resultado=a+b
    return resultado

def restar(var1, b):
    resul = var1-b
    return resul

if __name__ == '__main__':
    print("ESTE ALGORTIMO SUMA 2 NUMEROS")
    print ("Ingrese el primer numero")
    a= int(input())
    print("Ingrese el segundo numero")
    b= int(input())
    
    print ("MENU DE OPCIONES")
    print ("----------------")
    print ("1.- Sumar")
    print ("2.- Restar")
    print ("Ingrese su opcion: ")
    opcion = int(input())
    
    if(opcion==1):
        c = sumar(a,b)
        print ("El resultado de la suma de ", a ,"+",b," = ", c)
    elif(opcion==2):
        c= restar(a,b)
        print ("El resultado de la resta es:", c)