'''
Created on 24-04-2016

@author: David
'''

def restar (primerNumero, segundoNumero):
    resul = primerNumero - segundoNumero
    return resul

def sumar(num1, num2):
    total = num1 + num2
    return total

def multiplicar (num1, num2):
    resultado = num1 * num2
    return resultado

def dividir (num1,num2):
    resultado = num1 / num2
    return round(resultado)

if __name__ == '__main__':
    print("Ingrese el primer numero")
    a = int(input())
    print("Ingrese el segundo numero")
    b = int(input())
    print ("Seleccione Operacion Matematica")
    print ("         1.- Suma")
    print ("         2.- Resta")
    opc = int(input())
    if(opc==1):
        c = sumar(a, b)
        print ("El resultado de la suma es: ", c)
    elif(opc==2):
        c = restar(a,b)
        print ("El resultado de la resta es: ",c)
    
    
    
    