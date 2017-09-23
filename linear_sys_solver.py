import parser
from math import sin, cos, tan

#Graphs
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp
from mpl_toolkits.mplot3d import Axes3D

def solve_2D(formula, points = 100, increment=0.1):
    """
    takes a string representation of an equation and creates a tuple of lists with x and y data

    @param {str} formula - string representation of a 
    @param {int} points - The number of data points created, becareful of using too many
    @param {float} increment - distance between data points, smaller = more detailed, larger = faster

    @returns {tuple} - x_values, z_values, y_values
    """
    code = parser.expr(formula).compile()
    x_values = []

    y_values = []
    for x in [inc_x * increment for inc_x in range(0, points)]:
        x_values.append(x)
        y_values.append(eval(code))
    
    return x_values, y_values
def solve_3D(formula, points=100, increment=0.1):
    """
    takes a string representation of an equation and creates a tuple of lists with x, y, and z data

    @param {str} formula - string representation of a 
    @param {int} points - The number of data points created, becareful of using too many
    @param {float} increment - distance between data points, smaller = more detailed, larger = faster

    @returns {tuple} - x_values, z_values, y_values
    """
    code = parser.expr(formula).compile()
    x_values = []
    
    y_values = []
    z_values = []
    for x in [inc_x * increment for inc_x in range(0, points)]:
        for z in [inc_z * increment for inc_z in range(0, points)]:
            x_values.append(x)
            z_values.append(z)
            y_values.append(eval(code))
            

    return x_values, z_values, y_values


def graph_2D(data):
    """
    takes a tuple of data (x, y) and graphs it

    @param {tuple} data - (x_values, y_values) 

    @returns {matplotlib plt} 
    """

    plt.plot(data[0], data[1])
    return plt.show()

def graph_3D(data, mesh_value=10):
    """
    takes a tuple of data (x, y) and graphs it

    @param {tuple} data - (x_values, y_values) 
    @param {int} mesh_value - the number of meshes / area. larger = more detail
    
    @returns {matplotlib plt} 
    """

    plotx,ploty, = np.meshgrid(np.linspace(np.min(data[0]),np.max(data[1]),mesh_value),\
                           np.linspace(np.min(data[1]),np.max(data[1]),mesh_value))
    plotz = interp.griddata((data[0],data[1]),data[2],(plotx,ploty),method='linear')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.can_pan()
    ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap='viridis')
    return plt.show()


    