#!/usr/bin/env python
'''
Created on 23-04-2016

@author: David
'''
from pip._vendor.distlib.compat import raw_input


def siSimple():
    x=int (raw_input("Ingrese un numero, por favor:"))
    if(x==2):
        print ("Es el numero 2")

def siSinoSimple():
    x=int (raw_input("Ingrese un numero"))
    if(x==2):
        print ("Es el numero dos")
    else:
        print ("Es otro numero distinto que 2")
                  
def siSinoAnidado():
    x=int (raw_input("Ingrese un numero"))
    if x==2:
        print("Es el numero dos")
    elif(x==3):
        print("Es el numero tres")
    elif(x==4):
        print("Es el numero cuatro")
    else:
        print("Es otro numero")
          

if __name__ == '__main__':
    siSinoAnidado()
    