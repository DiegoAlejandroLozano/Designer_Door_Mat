'''
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''

def main():
    n, m = map(int, input('Ingrese N y M: ').split(' '))
    rango_medio = n//2
    contador = 0
    #rango superior
    for i in range(0, rango_medio):
        patron =  '.|.'*i + '.|.' + '.|.'*i
        print(patron.center(m, '-'))
    #imprimiendo en la mitad
    print('WELCOME'.center(m, '-'))
    #rango superior
    for i in range((rango_medio-1), -1, -1):
        patron =  '.|.'*i + '.|.' + '.|.'*i
        print(patron.center(m, '-'))

if __name__ == '__main__':
    main()
