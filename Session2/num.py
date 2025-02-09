import numpy as np

l1 = [1, 2, 3, 4, 5]
print(l1)
a1 = np.array(l1)
print(a1)

#generate array
a_zeros = np.zeros(5)
#2d
a_zeros = np.zeros((2, 3))
print(a_zeros)

a_ones = np.ones(5)
print(a_ones)

a_empty = np.empty(5)
print(a_empty)

a_arange = np.arange(5)
print(a_arange)

a_linspace = np.linspace(0, 10, 5)
print(a_linspace)

a_random = np.random.random(5)
print(a_random)

a_specific = np.full((5,5),7)
print(a_specific)

