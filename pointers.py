import numpy as np

### POINTER STUFF FOR NP ARRAYS 
x = np.array([0])
y = x
y = np.array([1])
print(x)
print(y)
y = x
y[0] = 1
print(x)
print(y)

# This outputs the following 
# [0]
# [1]
# [1]
# [1]

# To mitigate this do 

x = np.array([0])
y = x.copy()
y = np.array([1])
print(x)
print(y)
y = x.copy()
y[0] = 1
print(x)
print(y)
