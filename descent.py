from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from partialdev import *

def funcA():
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

def funcB():
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

def funcC():
    def f(x1, x2): 
        return 100*(x2-x1**2)**2+(x1-1)**2

    def plotter(E, A):
        alpha = float(input('Ingrese el tamaño para el paso: '))
        count = int(input('Ingrese el número de iteraciones: '))
        fig = plt.figure(figsize = [12, 8])
        ax = plt.axes(projection='3d')
        ax.plot_surface(X1, X2, f(X1, X2), cmap='jet', alpha=alpha)
        ax.plot_wireframe(X1, X2, f(X1, X2), rcount=15, ccount=count)
        # ax.view_init(elev=E, azim=A)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Rosenbrock 10-D function')
        ax.contourf(x1, x2, f(X1, X2))

    a = int(input('Ingrese el valor inicial para x1 : '))
    b = int(input('Ingrese el valor inicial para x2 : '))

    x1 = np.linspace(a,b)
    x2 = np.linspace(a,b)
    X1, X2 = np.meshgrid(x1, x2)
    F = f(x1, x2)
    plt.contour(X1, X2, f(X1, X2))
    plotter(45, 45)
    print(f'El minimo es: {F} en el punto: {X1, X2}')
    plt.show()
    

# if __name__ == '__main__':
#     rosenfunc()