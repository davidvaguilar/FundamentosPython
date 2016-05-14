'''
Created on 24-04-2016

@author: David
'''
def areaTriangulo (b,a):
    area= b *a/2
    return area

def areaCirculo (r):
    PI = 3.14
    area = PI*r**2
    return area

if __name__ == '__main__':
    print("ESTE ALGORITMO CALCULA EL AREA DE UN CIRCULO y DE UN TRIANGULO")
    print("Ingrese el radio del circulo")
    radio= int(input())
    print("El area del circulo ", areaCirculo(radio))
    print("Ingrese la base del triangulo")
    base=int(input())
    print("Ingrese la altura del triangulo")
    altura=int(input())
    print("El area del triangulo es: ", areaTriangulo(base, altura))
    
    
    
    