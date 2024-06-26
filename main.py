import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import funcs, integrals

ns = [5, 10, 20, 50, 100, 1000, 2000]
f_vec = np.vectorize(funcs.f)
F_vec = np.vectorize(funcs.F)
x = np.linspace(0, 5, 10000)
plt.figure(figsize=(10, 6))
plt.plot(x, f_vec(x), label='f(x)', color='blue')

for n in ns:
    plt.plot(x, funcs.f_n(x, n), label=f'f_{n}(x)', linestyle=':')

plt.xlabel('x')
plt.ylabel('f(x) & f_n(x)')
plt.legend()
plt.grid(True)
plt.show()

results = []
for n in ns:
    LI_int = integrals.LI(n)
    LSI_int = integrals.LSI(n, F_vec)
    results.append((n, LI_int, LSI_int))
    print(f'n = {n}: LI = {LI_int}, LSI = {LSI_int}')


results_df = pd.DataFrame(results, columns=['n', 'LI', 'LSI'])