# -*- coding: iso-8859-15 -*-

'''
Created on 23-04-2016

@author: David
'''


def textoSimple():
    print("Esto es un texto")
    
def tipoTexto():
    cadena="Esto es un texto"
    print (type(cadena))

def concadenarPalabras():
    cadena="Hola"+" Mundo"
    print(cadena)
    print(cadena.strip()+" Python")

def largoCadena():
    hola="Hola Mundo"
    print (len(hola))

# Comillas simples
def comillaSimple ():
    cadenaa = 'Texto entre comillas simples'
    print (cadenaa)

# Comillas dobles
def comillaDoble ():
    cadenab = "Texto entre".strip()+" comilla doble"
    print (cadenab)
    print (type(cadenab))

#Cadena multilinea
def cadenaMultilinea():
    cadenac = ("""Texto linea 1
    linea 2
    linea 3
    linea 4
    .
    .
    .
    .
    .
    linea N
    """)
    print (cadenac)
    print (type (cadenac))

def indexarCadena():
    palabra="Hola Mundo Python"
    print (palabra[0])
    print (palabra[0:2])
    print (palabra[2:6])
    print (palabra[:6])
    print (palabra[2:])
    print ('Nuevo '+palabra[2:])
    print ("Mas "+palabra[5])
    print (palabra[:2] + palabra[2:])
    print (palabra[:3] + palabra[3:])
    print (palabra [-2])
    print (palabra [:-2])

# Repeticion de cadena
def repetirCadena():
    cadrep = "Cadena" * 3
    print (cadrep*2)


def sacarComillas():
    print ("doesn\'t") #Imprimir comilla simple
    print ("\'Isn\'t,\' she said.") #Imprimir varias comillas simples
    print ('"Si," le dijo.')  #Imprimir varias comillas dobles

def saltoLinea():
    lineas= "Primera linea.\nSegunda linea." 
    #lineas='Hola \n Mundo'
    print (lineas)
    hola = "Esta es una larga cadena que contiene \n\
varias líneas de texto, tal y como se hace en C.\n\
        Notar que los espacios en blanco al principio de la linea\
son más significantes."
    print (hola)
    hola = r"Esta es una larga cadena que contiene\n\
varias líneas de texto, tal y como se hace en C."
    print (hola)

def sinSaltoLinea():
    salto=r"C:\algun\nombre"    #Comando r elimina la salida
    print (salto)

# Concatenacion de cadena
def concadenarCadena():
    nombre = ("Juan")
    apellido = ("Perez")
    nombre_completo = nombre + " " + apellido
    print (nombre_completo)
    print (type (nombre_completo))
    pass
    
def caracterUnicode():
    cadena=u'Hola\u0040Mundo!'
    print(cadena)
    
# acceder a rango de la cadena
def rangoCadena():
    nombre_completo=("Fernando Perez")
    print (nombre_completo[3:13])
    print ("Tamano de cadena '", nombre_completo, "' es:", len(nombre_completo))
    pass

if __name__ == '__main__':
    caracterUnicode()
    pass
    
    
    