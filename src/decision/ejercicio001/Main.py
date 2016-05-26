'''
Created on 05-05-2016

@author: David
'''

def DeterminarPositivo (a):
    if(a>0):
        return("El numero es positivo")
    else:
        if(a == 0):
            return ("Es 0")
        else:
            return("El numero es negativo")


if __name__ == '__main__':
    print ("ESTE PROGRAMA DETERMINA SI UN NUMERO ES POSITIVO SOLAMENTE")
    print ("Escriba un numero")
    num = int(input())
    r= DeterminarPositivo(num)
    print(r)
    