'''
Created on 06-05-2016

@author: David
'''
def NumeroMayor(a,b):
    if(a > b):
        resultado = "El valor", b, "es Mayor"
        return resultado
    else:
        resultado = "El valor", a, " es mayor"
        return resultado

if __name__ == '__main__':
   print  ("ESTE ALGORITMO DETERMINA EL MAYOR DE 2 NUMEROS")
   print ("Ingrese primer numero")
   num1= int(input())
   print ("Ingrese segundo numero")
   num2 = int (input())

   print(NumeroMayor(num1,num2))