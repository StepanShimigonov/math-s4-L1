import numpy as np


def f(x):
    x_str = str(x)
    if x_str.find('31415') != -1:
        return min(3 / 4, max(1 / 4, (x ** 2 - 1) ** 2))
    else:
        return np.sin(x)


def F(x):
    if 0 <= x <= 2:
        return np.sqrt(x)
    elif 2 < x <= 5:
        return x * np.floor(x)


def f_n(x, n):
    partitions = np.linspace(0, 5, n + 1)
    f_n_values = np.zeros_like(x)

    for i in range(n):
        mask = (x >= partitions[i]) & (x < partitions[i + 1])
        f_n_values[mask] = f(partitions[i])

    return f_n_values