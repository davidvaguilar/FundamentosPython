#!/usr/bin/env python
'''
Created on 16-04-2016

@author: David
'''

def suma():
    print(2+2)
    
def divisionFlotante():
    print (17/3)
    
def divisionEntera():
    print (17//3)

def divisionResto():
    print (17%3)
    
def potencia01():
    print (5**2)
    print (2**7)

def signoIgual():
    ancho=20
    largo=30
    print (ancho*largo)
    
def redondear():
    impuesto = 12.5 / 100
    precio = 100.50
    print (precio * impuesto)
    print (round(precio * impuesto,2))

def asignacionMultiple():
    x=y=z=0
    print (x,y,z)

def transformarAEntero():
    x=5.6
    print (int(x))
    
if __name__ == '__main__':
    transformarAEntero()
    
    a = "Holá"
    b = "mundo"
    c = 87
    d = 2.33145
    
    print(a, b)
    print("-{}-{}-".format(a, b))
    print("El resultado es:", c)
    print("El resultado es: {:d}min ({:d}seg)".format(c, c*60))