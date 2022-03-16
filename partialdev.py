# Funciones para encontrar derivadas parciales

def PartialDA ( point ):
    dx = (4*point[0])**3-4*point[1]
    dy = (4*point[1])**3+0.5-4*point[0]
    return dx, dy

def PartialDRosenbrock ( point ):
    dx = (-2*(1 - point[0]) - 400*(point[1] - (point[0]**2)**2))
    dy = 200*(point[1] - (point[0]**2))
    return dx, dy