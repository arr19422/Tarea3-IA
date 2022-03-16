''' 
Universidad del Valle de Guatemala
Inteligencia Artificial - Sección 20
Autores:
    Martín España   Carné: 19258
    Diego Arredondo Carné: 19422
    Alejandra Gudiel Carné: 19232
    Roberto Castillo  Carné: 18546
'''
from pprint import pprint
from algorithms import pathReader
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tsp import *
import descent as d

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
    print('Fecha: 15-03-2022')
    print('Versión: 1.0')
    print('----------------------------------- \n')

opcionMenu = 0
while opcionMenu != 3:
    print('1. Probar algoritmo de descenso máximo \n2. Probar el TSP \n3. Salir\n')

    opcionMenu = int(input('Ingrese una opción: '))
    
    if opcionMenu == 1:
        opcion1 = 0
        while opcion1 != 4:
            print('1. Utilizar función a - \n2. Utilizar función Rosenbruck 2D \n3. Utilizar función Rosenbrock 10D\n4. Salir\n')
            opcion1 = int(input('Ingrese una opción: '))
            if opcion1 == 1:
                d.funcA()
            pass
            if opcion1 == 2:
                d.funcB()
            pass
            if opcion1 == 3:
                d.funcC()
            pass
    pass

    if opcionMenu == 2:
        path = pathReader()
        tsp = TSP(path, path[0])
        tsp.getDistanceMatrix(path)
        tsp.calcDistance(tsp.path)
        tsp.calcTSP()
        tsp.printResults()
        pass
    else:
        print('Saliendo...')
        break
