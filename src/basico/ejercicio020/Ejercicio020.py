'''
Created on 05-05-2016

@author: David
'''

if __name__ == '__main__':
    print ("ESTE PROGRAMA CALCULA SU SALARIO SEMANAL ")
    print ("Ingrese el valor hora")
    valorHora = int(input())
    print("Ingrese la cantidad de Horas trabajadas")
    cantidadHora = int(input())
    salario = valorHora * cantidadHora
    print ("Su salario semanal es : ",salario)