'''
Created on 10-05-2016

@author: David
'''

if __name__ == '__main__':
    precio = float(input())
    if( precio >1000):
        precioConIva= round(precio*1.19)
        print("El precio con IVA es: ", precioConIva)
    else:
        print ("El precio es:", precio)
    