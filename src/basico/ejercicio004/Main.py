# -*- coding: iso-8859-15 -*-
import os
'''
Created on 24-04-2016

@author: David
'''



def sumar( num1, num2):
    resultado = num1+num2
    return resultado

def restar(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado =num1* num2
    return resultado
    
def dividir(num1, num2):
    resultado= num1/num2
    return resultado

def potencia(num1, num2):
    resultado =num1**num2
    return resultado

def modulo(num1,num2):
    resultado =num1%num2
    return resultado

if __name__ == '__main__':
    opc="-1"
    while(opc!="0"):
        print ("-------------------------------------------")
        print ("|           MENU PRINCIPAL                |")
        print ("-------------------------------------------")
        print ("|      1  sumar perro      SUMA          |")
        print ("|        2  -              RESTA          |")
        print ("|       M  m  *        MULTIPLICACION     |")
        print ("|     /  dividir         DIVISION         |")
        print ("|  potencia POTENCIA        POTENCIA      |")
        print ("|       mod      RESTO DE LA DIVISION     |")
        print ("|      0          SALIR DEL PROGRAMA      |")
        print ("-------------------------------------------")
        print ("Escoja una opcion del menu : ")
        opc = input()
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if(opc == "1" or opc == "sumar" or opc=="perro"):
            print("Ingrese el primer numero a sumar: ")
            num1 = int(input())
            print ("Ingrese el segundo numero a sumar: ")
            num2 = int(input())
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("        El resultado de la suma es: ", sumar(num1,num2) )
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif(opc == "2" or opc == "-"):
            print("Ingrese el primer numero a restar: ")
            num1=int(input())
            print ("Ingrese el segundo numero a restar: ")
            num2=int(input())
            print("--------------------------------------------------")
            print("        El resultado de la RESTA es: ", restar(num1,num2))
            print("--------------------------------------------------")
        elif(opc == "M" or opc == "m" or opc == "*"):
            print ("Ingrese el primer numero a multiplicar: ")
            num1 = int(input())
            print ("Ingrese el segundo numero a multiplicar: ")
            num2 = int(input())
            print("***************************************************")
            print("    El resultado de la MULTIPLICACION es: ", multiplicar(num1, num2))
            print("***************************************************")
        elif(opc == "/" or opc == "dividir"):
            print ("Ingrese el primer numero a dividir: ")
            num1 = int(input())
            print ("Ingrese el segundo numero a dividir: ")
            num2 = int(input())
            print("//////////////////////////////////////////////////")
            print("     El resultado de la DIVISION es: ", dividir(num1, num2))
            print("//////////////////////////////////////////////////")
        elif(opc=="potencia" or opc == "POTENCIA"):
            print ("Ingrese la base de la potencia: ")
            num1=int(input())
            print ("Ingrese el exponente de la potencia")
            num2= int(input())
            total= potencia(num1, num2)
            print("**************************************************")
            print ("   El resultado de la POTENCIA es: ", total);
            print("**************************************************")
        elif(opc=="mod"):
            print ("Ingrese el primer numero de la operacion")
            num1=int(input())
            print ("Ingrese el segundo numero de la operacion")
            num2=int(input())
            total=modulo(num1,num2)    
            print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print( "El resultado del resto de la division es :", total)
            print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        elif(opc=="0"):
            pass
        else:
            print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
            print("SR. USUARIO SU OPCION NO ES VALIDA, VUELVA A INTENTAR")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("...........................................")
    print(" HA TERMINADO EL PROGRAMA, VUELVA PRONTO")
    print("...........................................")
    
    
    
    
    
    
    
    