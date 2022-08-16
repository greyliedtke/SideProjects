"""
Script to convert array into path for stepper / leds to follow

"""
import numpy as np
from SimulateAnimate.animating import simulate_path


# dummy array to be using
d_array = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0]
]


# format matrix into a conventional xy format
def format_mat(mat):
    ar = np.array(d_array)
    mat = np.matrix(d_array)
    mat = mat.transpose()
    mat = np.flip(mat, 1)
    return mat


# format matrix and return values of all 1 states
d_mat = format_mat(d_array)
x_cords, y_cords = np.where(d_mat == 1)
print(x_cords, y_cords)


# simulate path from
simulate_path(x_cords, y_cords)


# def create_path():
#     for

# end of script
