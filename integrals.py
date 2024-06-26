import numpy as np
import funcs

def LI(n):
    partitions = np.linspace(0, 5, n + 1)
    integral_sum = 0
    for i in range(n):
        x_i = partitions[i]
        delta_x = partitions[i + 1] - partitions[i]
        integral_sum += funcs.f_n(x_i, n) * delta_x
    return integral_sum


def LSI(n, F_vec):
    partitions = np.linspace(0, 5, n + 1)
    integral_sum = 0
    for i in range(n):
        x_i = partitions[i]
        integral_sum += funcs.f_n(x_i, n) * (F_vec(partitions[i + 1]) - F_vec(partitions[i]))
    return integral_sum

