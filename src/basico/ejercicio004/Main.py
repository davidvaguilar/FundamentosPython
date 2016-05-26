# -*- coding: iso-8859-15 -*-
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


if __name__ == '__main__':
    
    print ("-------------------------------------------")
    print ("|           MENU PRINCIPAL                |")
    print ("-------------------------------------------")
    print ("|      1  sumar      Sumar                |")
    print ("|        2  -          Restar             |")
    print ("|       M  m  *         Multiplicar       |")
    print ("|     /  dividir    Dividir               |")
    print ("-------------------------------------------")
    print ("Escoja una opcion del menu : ")
    opc = input()
    if(opc == "1" or opc == "sumar"):
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
    else:
        print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
        print("SR. USUARIO SU OPCION NO ES VALIDA, VUELVA A INTENTAR")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("...........................................")
    print(" HA TERMINADO EL PROGRAMA, VUELVA PRONTO")
    print("...........................................")
    
    
    
    
    
    
    
    