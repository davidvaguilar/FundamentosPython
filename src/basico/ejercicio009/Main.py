'''
Created on 24-04-2016

@author: David
'''

if __name__ == '__main__':
    print ("Ingrese el primero numero")
    numero1 = int (input())
    print ("Ingrese el segundo numero")
    numero2 = int (input())
    cuocienteFlotante = numero1 / numero2
    coucienteEntero = numero1 // numero2
    resto = numero1 % numero2
    print ("El cuociente con punto flotante es: ",cuocienteFlotante)
    print ("El cuociente sin punto flotante es: ", coucienteEntero)
    print ("El couciente redondeado es: ", round(cuocienteFlotante))
    print ("El resto de la division es: ", resto)