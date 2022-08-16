"""
Script to animate using matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np


# function used for simulating stuff
def fun_func(x_ar):
    y_out = []
    for x in x_ar:
        y = (x-1) * (x - 3) * (x - 6)
        y_out.append(y)
    return y_out


# array manipulation
x_ar = list(range(0, 100))
x_ar = np.array(x_ar)
x_ar = x_ar/10
y_ar = fun_func(x_ar)


plt.axis([0, 10, 0, 10])

x_path = [0, 7, 2, 6, 4, 5]
y_path = [1, 5, 10, 3, 2, 1]


# for i in range(len(x_ar)):
#
#     plt.plot(x_ar[0:i], y_ar[0:i], 'b')
#     plt.pause(0.001)
#
# plt.show()


def simulate_path(x_list, y_list):

    # set plot size
    plt.axis([min(x_list)-1, max(x_list)+1, min(y_list)-1, max(y_list)+1])

    # loop through array to simulate plots
    for i in range(len(x_list)+1):
        # plt.plot(x_list[0:i], y_list[0:i], 'b')
        plt.scatter(x_list[0:i], y_list[0:i], c='b', s=100)
        plt.pause(.25)
    plt.show()



# end of script
