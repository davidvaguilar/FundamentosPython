'''
Created on 06-05-2016

@author: David
'''

if __name__ == '__main__':
    print ("ESTE PROGRAMA DETERMINA SI EL RESULTADO DE LA SUMA ES CORRECTO")
    print ("Ingrese primer numero")
    num1= int(input())
    print ("Ingrese segundo numero")
    num2= int(input())
    print ("Cual cree que es el resultado??")
    calculoUsuario = int(input())
    
    resultado = num1 + num2
    if(resultado == calculoUsuario):
        print ("El calculo es correcto")
    else:
        print("Su calculo mental fallo: el resultado ",resultado )
        