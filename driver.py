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
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tsp import *
from partialdev import *

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
    print('1. Probar algoritmo de descenso m´aximo - \n2. Probar el TSP \n3. Salir\n')

    opcionMenu = int(input('Ingrese una opción: '))
    
    if opcionMenu == 1:
        opcion1 = 0
        while opcion1 != 3:
            print('1. Utilizar función a - \n2. Utilizar función Rosenbruck 2D \n3. Salir\n')
            opcion1 = int(input('Ingrese una opción: '))
            if opcion1 == 1:
                paso = float(input('Ingrese el tamaño de paso : '))
                x0 = float(input('Ingrese el valor inicial para x0 : '))
                y0 = float(input('Ingrese el valor inicial para y0 : '))
                a = np.array([x0, y0])
                aiter = []
                iterations = int(input('Ingrese el número de iteraciones : '))
                for i in range(iterations):
                     f = (a[0]**4+a[1]**4-4*a[0]*a[1]+(0.5*a[1])+1)
                     aiter.append([a,f])
                     fi = np.array(PartialDA(a))
                     a = a - np.dot(paso,fi)
                aiter = np.array(aiter)
                print(aiter)
                print(f'El minimo es: {aiter[-1, 1]} en el punto: {aiter[-1,0]}')
                fig = plt.figure(figsize=(10, 8))
                ax = fig.gca(projection='3d')
                ax.set_title('3D surface plot of Function A')
                ax.set_xlabel('x axis')
                ax.set_ylabel('y axis')
                ax.set_zlabel('z axis')

                x = np.arange(-10, 10, 0.05)
                y = np.arange(-10, 10, 0.05)
                x, y = np.meshgrid(x, y)
                f = x**4+y**4-4*x*y+(0.5*y)+1

                surface = ax.plot_surface(x, y, f, cmap=cm.coolwarm, linewidth=0)
                fig.colorbar(surface, shrink=0.5)

                plt.show()
            pass
            if opcion1 == 2:
                paso = float(input('Ingrese el tamaño de paso : '))
                x0 = float(input('Ingrese el valor inicial para x1 : '))
                y0 = float(input('Ingrese el valor inicial para x2 : '))
                a = np.array([x0, y0])
                aiter = []
                iterations = int(input('Ingrese el número de iteraciones : '))
                for i in range(iterations):
                     f = ((1 - a[0])**2) + (100*((a[1] - a[0]**2)**2))
                     aiter.append([a,f])
                     fi = np.array(PartialDRosenbrock(a))
                     a = a - np.dot(paso,fi)
                aiter = np.array(aiter)
                print(aiter)
                print(f'El minimo es: {aiter[-1, 1]} en el punto: {aiter[-1,0]}')
                fig = plt.figure(figsize=(10, 8))
                ax = fig.gca(projection='3d')
                ax.set_title('3D surface plot of Rosenbruck function')
                ax.set_xlabel('x1 axis')
                ax.set_ylabel('x2 axis')
                ax.set_zlabel('x3 axis')

                x = np.arange(-10, 10, 0.05)
                y = np.arange(-10, 10, 0.05)
                x, y = np.meshgrid(x, y)
                f = 100*(x**2-2*x*y*2+y*4)+(1-x+x**2)

                surface = ax.plot_surface(x, y, f, cmap=cm.coolwarm, linewidth=0)
                fig.colorbar(surface, shrink=0.5)

                plt.show()
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
