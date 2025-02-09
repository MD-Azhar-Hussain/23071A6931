import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

print("Vertical Stack\n", np.vstack((a,b)))
print("Horizontal Stack", np.hstack((a,b)))

#unique elements


c = np.array([1,2,3,4,5,1,2,3,4,5])
print("Unique elements: ", np.unique(c))