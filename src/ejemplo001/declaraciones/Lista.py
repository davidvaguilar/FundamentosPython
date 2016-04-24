'''
Created on 24-04-2016

@author: David
'''

def declarandoLista():
    a = ['pan', 'huevos', 100, 1234]
    print (a)

def indexarLista():
    a = ['pan', 'huevos', 100, 1234]
    print (a[3])
    print (a[1:-1])
    print (a[:2]+["carne",2*2])
    print (3*a[:3] + ["Boo!"])
    
def concadenar():
    a = ['pan', 'huevos', 100, 1234]
    a[2] = a[2] + 23
    print (a)

if __name__ == '__main__':
    concadenar()