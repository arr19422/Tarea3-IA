''' 
Universidad del Valle de Guatemala
Inteligencia Artificial - Sección 20
Autores:
    Martín España   Carné: 19258
    Diego Arredondo Carné: 19422
    Alejandra Gudiel Carné: 19232
'''
from pprint import pprint
from algorithms import pathReader

# TODO Change this to True when program is finished
showBanner = False
if showBanner:
    # Print banner
    print('|||      |||  \\\            ///  ||||||||||||')
    print('|||      |||   \\\          ///   |||')
    print('|||      |||    \\\        ///    |||')
    print('|||      |||     \\\      ///     |||  |||||||')
    print('|||      |||      \\\    ///      |||      |||')
    print('|||      |||       \\\  ///       |||      |||')
    print('||||||||||||        \\\///        ||||||||||||')
    print('-----------------------------------')
    print('Universidad del Valle de Guatemala')
    print('Inteligencia Artificial - Sección 20')
    print('Autores:')
    print('     Martín España     Carné: 19258')
    print('     Diego Arredondo   Carné: 19422')
    print('     Alejandra Gudiel  Carné: 19232')
    print('Fecha: 24-02-2022')
    print('Versión: 1.0')
    print('----------------------------------- \n')

opcionMenu = 0
while opcionMenu != 3:
    print('1. Probar - \n2. Probar el TSP \n3. Salir\n')

    opcionMenu = int(input('Ingrese una opción: '))
    
    if opcionMenu == 1:
        pass

    if opcionMenu == 2:
        pathReader()
        pass
    else:
        print('Saliendo...')
        break
