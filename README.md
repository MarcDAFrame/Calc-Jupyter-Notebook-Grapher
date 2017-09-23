# Calc-Jupyter-Notebook-Grapher
Converts string representations of equations to matplotlib graphs or tuples of lists of data using this 

2D or 3D graphs

## Examples of input

| 2*x + 1  | sin(x) | sin(x+z) | sin(5*x)*cos(5*z)/5 |
| ------------- | ------------- | ------------- | ------------- |
| <img src="https://github.com/MarcDAFrame/Calc-Jupyter-Notebook-Grapher/blob/master/git%20imgs/2x%2B1.png" width="200" height="150">  | <img src="https://github.com/MarcDAFrame/Calc-Jupyter-Notebook-Grapher/blob/master/git%20imgs/sin(x).png" width="200" height="150">  | <img src="https://github.com/MarcDAFrame/Calc-Jupyter-Notebook-Grapher/blob/master/git%20imgs/sin(x%2Bz).png" width="200" height="150"> | <img src="https://github.com/MarcDAFrame/Calc-Jupyter-Notebook-Grapher/blob/master/git%20imgs/sin(5*x)*cos(5*z)%205.png" width="200" height="150"> | 
| | | |

## Methods
  **- solve_2D(formula, points = 100, increment=0.1)**
    
    takes a string representation of an equation and creates a tuple of lists with x and y data

    @param {str} formula - string representation of a linear system f(x)

    @param {int} points - The number of data points created, becareful of using too many

    @param {float} increment - distance between data points, smaller = more detailed, larger = faster

    @returns {tuple} - x_values, z_values, y_value
    
  **-solve_3D(formula, points=100, increment=0.1)**
  
    takes a string representation of an equation and creates a tuple of lists with x, y, and z data

    @param {str} formula - string representation of a system of equation f(x,z)

    @param {int} points - The number of data points created, becareful of using too many

    @param {float} increment - distance between data points, smaller = more detailed, larger = faster

    @returns {tuple} - x_values, z_values, y_values
    
  **-graph_2D(data)**

    takes a tuple of data (x, y) and graphs it

    @param {tuple} data - (x_values, y_values) 

    @returns {matplotlib plt}
  
  **-graph_3D(data, mesh_value=10)**
  
    takes a tuple of data (x, y) and graphs it
    
    @param {tuple} data - (x_values, y_values) 
    
    @param {int} mesh_value - the number of meshes / area. larger = more detail

    @returns {matplotlib plt} 
