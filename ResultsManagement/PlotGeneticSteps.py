
import random
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt
import re

combinations = [('rmsd','gdt_2'),('rmsd','gdt_4'),
                ('rmsd','maxsub'),('rmsd','tm'),
                ('gdt_2','gdt_4'),('gdt_2','maxsub'),
                ('gdt_2','tm'), ('gdt_4','maxsub'),
                ('gdt_4','tm'), ('maxsub','tm')]

xs = []
ys = []

for m1, m2 in combinations:
    print(m1+' '+m2)

    # read respective files from genetic algorithm
    with open('C:/ShareSSD/scop/tests/complete_a.1._rmsd_gdt_2', 'r') as fp:

        x = []
        y = []

        line = fp.readline()
        while line:

            # get best individual from a generation
            if 'Generation:' in line:
                values = re.findall(r'-?\d+\.?\d*', line)
                x.append(float(values[0]))
                y.append(float(values[1]))

            line = fp.readline()

    xs.append(x)
    ys.append(y.sort())

    break


plt.step(x, y, label='test')

plt.legend()

plt.xlim(0, 10)
plt.ylim(0, 100)

plt.show()