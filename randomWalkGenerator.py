import matplotlib.pyplot as plt
import numpy as np
import random as rd

def random_walk_generator_1D(n):
    # initial coords
    x = [0]
    y = [0]
    for i in range(0, n, 1):
        step = rd.randint(-9, 10)
        coord = rd.randint(0, 2)
        if i%2 == 0:
            x.append(step+x[-1])
        else:
            y.append(step+y[-1])
    print(x)
    print(y)
    plt.scatter(x, y) 
    plt.show() 
    


random_walk_generator_1D(100)

# x = [1, 2, 3, 4, 5, 6, 7, 8] 
# y = [2, 3, 1, 3, 1, 4, 2, 3] 

# plt.scatter(x, y) 
# plt.show() 