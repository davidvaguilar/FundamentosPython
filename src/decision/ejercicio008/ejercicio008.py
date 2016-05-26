'''
Created on 24-05-2016

@author: David
'''
from nt import truncate

if __name__ == '__main__':
    opcion=0
    
    while(opcion != 2):
        print ("---------------------------------------")
        print ("        MENU PRINCIPAL")
        print ("---------------------------------------")
        print (" 1.- Ingresar el sueldo del trabajador")
        print (" 2.- Salir del programa")
        print ("---------------------------------------")
        print ("Ingrese solamente una opcion: ")
        opcion = int(input())
        if(opcion==1):
            print ("Ingrese el nombre del trabajador")
            nombre = input()
            print ("Ingrese el sueldo del trabajador : ", nombre)
            sueldo = int(input())
            if(sueldo > 500000):
                sueldoConAumento = sueldo * 1.12
                print ("El sueldo con aumento de ", nombre, " es de : ", round(sueldoConAumento))
                print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                sueldoConAumento= sueldo * 1.15
                print ("El sueldo con aumento de ", nombre, " es de : ", round(sueldoConAumento))
                print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif(opcion==2):
            print ("Esta saliendo del programa........")
        else:
            print ("Sr. Usuario, la opcion no es valida")
    print("----------------------------------------")
    print ("El programa ha terminado, vuelva pronto")
    print("----------------------------------------")
    